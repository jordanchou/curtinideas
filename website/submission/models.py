from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

id = 0

#-----------------------------------------------------------------------------

class Submission(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('accounts.CustomUser')

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.PositiveSmallIntegerField(default=0)
    downvotes = models.PositiveSmallIntegerField(default=0)
    num_views = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(max_length=50)

    def post(self):
        self.published_date = timezone.now()
        self.num_views = 0
        self.upvotes = 0
        self.downvotes = 0
        id = id + 1
        self.save()

    def __str__(self):
        return self.title

    def get_score(self):
        if ( (self.upvotes - self.downvotes) < 0 ):
            return 0

        return (self.upvotes - self.downvotes)

    def get_upvotes(self):
        return self.upvotes

    def get_downvotes(self):
        return self.downvotes


#-----------------------------------------------------------------------------

class Comment(models.Model):
    submission = models.ForeignKey('submission.Submission', related_name='comments', default = 0)
    author = models.ForeignKey('accounts.CustomUser', default=0)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    is_improvement = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

#    def delete_comment(self):
#        Comment.objects.filter(self.pk).delete()

#-----------------------------------------------------------------------------
