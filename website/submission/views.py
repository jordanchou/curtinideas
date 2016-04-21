from .models import Submission, Comment
from accounts.models import CustomUser
from .forms import SubmissionForm, CommentForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

#-----------------------------------------------------------------------------

def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    return render(request, 'submission/submission_detail.html', {'submission': submission})

#-----------------------------------------------------------------------------

def submission_list(request):
    submissions = Submission.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

def submission_list_upvotes(request):
    submissions = Submission.objects.order_by('-upvotes')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

def submission_list_downvotes(request):
    submissions = Submission.objects.order_by('-downvotes')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

def submission_list_num_views(request):
    submissions = Submission.objects.order_by('-num_views')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

#[submission_list_author description]
#@param  {[type]} request [description]
#@return {[type]}         [description]
def submission_list_author(request):
    submissions = Submission.objects.order_by('-author')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

def submission_list_self(request, slug):
    submissions = Submission.objects.filter(author__email=slug)

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

def submission_create(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return submission_list(request)
    else:
        form = SubmissionForm()

    return render(request, 'submission/submission_create.html', {'form': form})

#-----------------------------------------------------------------------------

def update_upvotes(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    upvote = submission.get_upvotes()
    submission_vote = Submission.objects.filter(pk=submission.pk).update(upvotes=upvote+1)

    return submission_list(request)

#-----------------------------------------------------------------------------

def update_downvotes(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    downvote = submission.get_downvotes()
    submission_vote = Submission.objects.filter(pk=submission.pk).update(downvotes=downvote+1)

    return submission_list(request)

#-----------------------------------------------------------------------------

def submission_delete(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    submission.delete()

    submissions = Submission.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'submission/submission_list.html', {'submissions': submissions})

#-----------------------------------------------------------------------------

def submission_edit(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if request.method == "POST":
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
            submission.published_date = timezone.now()
            submission.save()
            return redirect('/submission/', pk=submission.pk)
    else:
        form = SubmissionForm(instance=submission)
    return render(request, 'submission/submission_create.html', {'form': form})

#-----------------------------------------------------------------------------

def comment_on_submission(request, slug, pk):
    submission = get_object_or_404(Submission, pk=pk)
    author = get_object_or_404(CustomUser, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.submission = submission
            comment.author = author
            comment.save()

            return render(request, 'submission/submission_detail.html', {'submission': submission})
    else:
        form = CommentForm()

    return render(request, 'submission/comment_on_submission.html', {'form' : form})

#-----------------------------------------------------------------------------


def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    submission = get_object_or_404(Submission, pk=comment.submission.pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.submission = submission
            comment.author = request.user
            comment.save()
            return render(request, 'submission/submission_detail.html', {'submission': submission})
    else:
        form = CommentForm(instance=comment)
    return render(request, 'submission/comment_on_submission.html', {'form' : form})

#-----------------------------------------------------------------------------

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    submission = comment.submission.pk
    comment.delete()

    submission = get_object_or_404(Submission, pk=submission)
    return render(request, 'submission/submission_detail.html', {'submission' : submission})
