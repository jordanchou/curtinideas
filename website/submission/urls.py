from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^$', views.submission_list, name = 'submission_list'),
                url(r'^submit/$', views.submission_new, name='submission_new'),

              ]