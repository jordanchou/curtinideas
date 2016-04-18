from .models import Submission
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

#def submission_edit(request, id):
#    instance = Submission.objects.get(id=id)
#    form = SubmissionForm(request.POST or None, instance=instance)
#    if form.is_valid():
#          form.save()
#          return redirect('next_view')
#    return direct_to_template(request, 'submission/submission_detail.html', {'form': form}

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