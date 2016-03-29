from .models import Submission
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
# 
def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    return render(request, 'submission/submission_detail.html', {'submission': submission})

def submission_list(request):
    submissions = Submission.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_list_upvotes(request):
    submissions = Submission.objects.order_by('upvotes')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_list_downvotes(request):
    submissions = Submission.objects.order_by('downvotes')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_list_num_views(request):
    submissions = Submission.objects.order_by('num_views')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

def submission_list_author(request):
    submissions = Submission.objects.order_by('author')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})

