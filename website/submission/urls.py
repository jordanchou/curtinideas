from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^submission(?P<pk>\d+)/$', views.submission_detail, name='submission_detail'),
                url(r'^$', views.submission_list, name = 'submission_list'),
                url(r'^submit/$', views.submission_create, name='submission_create'),
                url(r'^submission/(?P<slug>.*)/$', views.submission_list_self, name='account_submission'),
                url(r'^upvotes(?P<pk>\d+)/$', views.update_upvotes, name='submission_upvotes'),
                url(r'^downvotes(?P<pk>\d+)/$', views.update_downvotes, name='submission_downvotes'),
              ]