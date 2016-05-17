from django.contrib import admin
from .models import Submission, Comment, SubVoting, ComVoting

#-----------------------------------------------------------------------------

admin.site.register(Submission)
admin.site.register(Comment)
admin.site.register(SubVoting)
admin.site.register(ComVoting)
