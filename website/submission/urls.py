from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^submission(?P<pk>\d+)/$', views.submission_detail, name='submission_detail'),
                url(r'^$', views.submission_list, name = 'submission_list'),
                url(r'^submit/$', views.submission_create, name='submission_create'),
              ]