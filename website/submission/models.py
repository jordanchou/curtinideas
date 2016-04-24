from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

id = 0

#-----------------------------------------------------------------------------
CATEGORIES = (
    ('Science and Engineering', 'Science and Engineering'),
    ('Health Sciences', 'Health Sciences'),
    ('Humanities', 'Humanities'),
)

class Submission(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('accounts.CustomUser')

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.PositiveSmallIntegerField(default=0)
    downvotes = models.PositiveSmallIntegerField(default=0)
    num_views = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    links = models.CharField(max_length=200, null=True)

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

    def increase_view(self):
        self.num_views = self.num_views + 1
    def get_links(self):
    	return self.links

#-----------------------------------------------------------------------------

class Comment(models.Model):
    submission = models.ForeignKey('submission.Submission', related_name='comments', default = 0)
    author = models.ForeignKey('accounts.CustomUser', default=0)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    is_improvement = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    upvotes = models.PositiveSmallIntegerField(default=0)
    downvotes = models.PositiveSmallIntegerField(default=0)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_score(self):
        if ( (self.upvotes - self.downvotes) < 0 ):
            return 0

        return (self.upvotes - self.downvotes)

    def get_upvotes(self):
        return self.upvotes

    def get_downvotes(self):
        return self.downvotes

#    def delete_comment(self):
#        Comment.objects.filter(self.pk).delete()

#-----------------------------------------------------------------------------

class SubVoting(models.Model):
    submission = models.ForeignKey('submission.Submission', related_name='subvotes', default = 0)
    voter = models.ForeignKey('accounts.CustomUser')
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)

    def create_sub_up_vote(self, submission, voter):
        self.submission = submission
        self.voter = voter
        self.upvote = True
        self.save()

    def create_sub_down_vote(self, submission, voter):
        self.submission = submission
        self.voter = voter
        self.downvote = True
        self.save()

    def __str__(self):
        identifier = "SUBMISSION: " + self.submission.title + "USER: " + self.voter.email  
        return identifier       
        
#-----------------------------------------------------------------------------

class ComVoting(models.Model):
    submission = models.ForeignKey('submission.Submission', related_name='comvotes', default = 0)
    comment = models.ForeignKey('submission.Comment', related_name='comvotes', default = 0)
    voter = models.ForeignKey('accounts.CustomUser')
    upVote = models.BooleanField(default=False)
    downVote = models.BooleanField(default=False)

    def create_com_up_vote(self, comment, voter):
        self.submission = comment.submission
        self.comment = comment
        self.voter = voter
        self.upvote = True
        self.save()

    def create_com_down_vote(self, comment, voter):
        self.submission = comment.submission
        self.comment = comment
        self.voter = voter
        self.downvote = True
        self.save()

    def __str__(self):
        identifier = " SUBMISSION: " + self.submission.title + " COMMENT: " + str(self.comment.pk)
        identifier = identifier + " USER: " + self.voter.email 
        return identifier   
        
#-----------------------------------------------------------------------------