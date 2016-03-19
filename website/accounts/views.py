from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import CustomUser


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = CustomUser

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(CustomUser.objects.make_random_password())
        obj.save()

        #reset_form = PasswordResetForm(self.request.POST)
        #reset_form.is_valid()
        
        # Copied from django/contrib/auth/views.py : password_reset
        #opts = {
        #   'use_https': self.request.is_secure(),
        #    'email_template_name': 'accounts/verification.html',
        #    'subject_template_name' : 'accounts/verification_subject.html',
        #    'request': self.request,
        #        }
        # This form sends the email on save()
        #reset_form.save(**opts)

        return redirect('accounts:register-done')

