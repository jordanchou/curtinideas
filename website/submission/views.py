from .models import Submission, Comment, SubVoting, ComVoting
from accounts.models import CustomUser
from .forms import SubmissionForm, CommentForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, RequestContext
from . import searchfunctions

#-----------------------------------------------------------------------------

def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    submission.increase_view()

    submission.save()

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
#
def submission_list_score(request):
    submissions = list(Submission.objects.all())
    submissions = sorted(submissions, key = lambda s:s.get_score(), reverse=True)

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

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

def update_sub_upvotes(request, slug, pk):
    submission = get_object_or_404(Submission, pk=pk)
    voter = get_object_or_404(CustomUser, slug=slug)

    new_vote = SubVoting();
    new_vote.create_sub_up_vote(submission, voter)

    upvote = submission.get_upvotes()
    submission_vote = Submission.objects.filter(pk=submission.pk).update(upvotes=upvote+1)

    return submission_list(request)

#-----------------------------------------------------------------------------

def update_sub_downvotes(request, slug, pk):
    submission = get_object_or_404(Submission, pk=pk)
    voter = get_object_or_404(CustomUser, slug=slug)

    new_vote = SubVoting();
    new_vote.create_sub_down_vote(submission, voter)

    downvote = submission.get_downvotes()
    submission_vote = Submission.objects.filter(pk=submission.pk).update(downvotes=downvote+1)

    return submission_list(request)

#-----------------------------------------------------------------------------

def update_com_upvotes(request, slug, pk):
    comment = get_object_or_404(Comment, pk=pk)
    voter = get_object_or_404(CustomUser, slug=slug)

    new_vote = ComVoting();
    new_vote.create_com_up_vote(comment, voter)

    upvote = comment.get_upvotes()
    comment_vote = Comment.objects.filter(pk=comment.pk).update(upvotes=upvote+1)

    submission = comment.submission
    return render(request, 'submission/submission_detail.html', {'submission': submission})

#-----------------------------------------------------------------------------

def update_com_downvotes(request, slug, pk):
    comment = get_object_or_404(Comment, pk=pk)
    voter = get_object_or_404(CustomUser, slug=slug)

    new_vote = ComVoting();
    new_vote.create_com_up_vote(comment, voter)

    downvote = comment.get_downvotes()
    comment_vote = Comment.objects.filter(pk=comment.pk).update(downvotes=downvote+1)

    submission = comment.submission
    return render(request, 'submission/submission_detail.html', {'submission': submission})

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

def submission_list_science_and_eng(request):
    submissions = Submission.objects.filter(category = "Science and Engineering")

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_list_health_sciences(request):
    submissions = Submission.objects.filter(category = "Health Sciences")

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_list_humanities(request):
    submissions = Submission.objects.filter(category = "Humanities")

    return render(request, 'submission/submission_list.html', {'submissions': submissions})


#-----------------------------------------------------------------------------

################## search
def search(request):
    query_string = ''
    submissions = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = searchfunctions.get_query(query_string, ['title', 'text'])

        submissions = Submission.objects.filter(entry_query).order_by('-published_date')

    return render_to_response('submission/submission_list.html',
                          { 'submissions': submissions },
                          context_instance=RequestContext(request))


#-----------------------------------------------------------------------------

def update_comment_upvotes(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    upvote = comment.upvotes
    comment_vote = Comment.objects.filter(pk=comment.pk).update(upvotes=upvote+1)
    submission = comment.submission
    return render(request, 'submission/submission_detail.html', {'submission': submission})

#-----------------------------------------------------------------------------

def update_comment_downvotes(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    downvote = comment.downvotes
    comment_vote = Comment.objects.filter(pk=comment.pk).update(downvotes=downvote+1)
    submission = comment.submission
    return render(request, 'submission/submission_detail.html', {'submission': submission})

#-----------------------------------------------------------------------------