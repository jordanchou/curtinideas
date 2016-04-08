from django.conf.urls import url

from .views import RegistrationView, AccountDetailView, AccountUpdateView
from django.contrib.auth import views
from django.contrib.auth.views import login, logout, password_change, password_change_done

urlpatterns = [
                url(r'^login/$', 'django.contrib.auth.views.login', name='login',
                    kwargs={'template_name': 'accounts/login.html'}
                   ),

                url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',
                    kwargs={'next_page': '/'}
                   ),

                url(r'^password_change$',
                    'django.contrib.auth.views.password_change',
                    name='password_change',
                    kwargs={
                            'template_name':'accounts/password_change_form.html',
                            'post_change_redirect':'accounts:password_change_done',
                           }
                   ),

                url(r'^password_change_done$',
                    'django.contrib.auth.views.password_change_done',
                    name='password_change_done',
                    kwargs={'template_name':'accounts/password_change_done.html'}
                   ),

                url(r'^register/$', RegistrationView.as_view(), name='register'),
                url(r'^register/done/$', views.password_reset_done,
                {
                    'template_name' : 'registration/initial_done.html',
                },
                name='register-done'),

                url(r'^register/password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
                views.password_reset_confirm, 
                {
                    'template_name': 'registration/initial_confirm.html',
                    'post_reset_redirect': 'accounts:register-complete',
                }, name='register-confirm'),
                url(r'^register/complete/$', 
                views.password_reset_complete, {
                'template_name': 'registration/.html',
                 }, name='register-complete'),

                 url(r'^profile/(?P<slug>.*)/$', AccountDetailView.as_view(), name='account_detail'),
                 url(r'^profile/edit/(?P<slug>.*)/$', AccountUpdateView.as_view(), name='get'),
               ]
                 
            
