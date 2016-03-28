from django.shortcuts import render
from .models import Submission
from django.utils import timezone

# Create your views here.
def submission_list(request):
    submissions = Submission.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'submission/submission_list.html', {'submissions': submissions})