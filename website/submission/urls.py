from django.conf.urls import url
from . import views

#-----------------------------------------------------------------------------

urlpatterns = [
                url(r'^submission/(?P<pk>.*)/comment/(?P<slug>.*)/$', views.comment_on_submission, name='comment_on_submission'),
                url(r'^(?P<pk>\d+)/$', views.submission_detail, name='submission_detail'),
                url(r'^$', views.submission_list, name = 'submission_list'),
                url(r'^sort_by_date/$', views.submission_list, name = 'submission_list'),
                url(r'^sort_by_author/$', views.submission_list_author, name = 'submission_list_author'),
                url(r'^sort_by_upvotes/$', views.submission_list_upvotes, name = 'submission_list_upvotes'),
                url(r'^sort_by_downvotes/$', views.submission_list_downvotes, name = 'submission_list_downvotes'),
                url(r'^sort_by_views/$', views.submission_list_num_views, name = 'submission_list_num_views'),
                url(r'^submit/$', views.submission_create, name='submission_create'),
                url(r'^submission/(?P<slug>.*)/$', views.submission_list_self, name='account_submission'),
                url(r'^upvotes(?P<pk>\d+)/$', views.update_upvotes, name='submission_upvotes'),
                url(r'^downvotes(?P<pk>\d+)/$', views.update_downvotes, name='submission_downvotes'),
                url(r'^delete/(?P<pk>.*)/$', views.submission_delete, name='submission_delete'),
                url(r'^comment/edit/(?P<pk>.*)/$', views.comment_edit, name='comment_edit'),
                url(r'^comment/delete/(?P<pk>.*)/$', views.comment_delete, name='comment_delete'),
                url(r'^edit/(?P<pk>.*)/', views.submission_edit, name='submission_edit'),

              ]

#-----------------------------------------------------------------------------
