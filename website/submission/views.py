from django.shortcuts import render
from .models import Submission
from .forms import SubmissionForm
from django.utils import timezone

# Create your views here.
def submission_list(request):
    submissions = Submission.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_new(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('view_submissions')
    else:
        form = SubmissionForm()
    return render(request, 'submission/submission_edit.html', {'form': form})