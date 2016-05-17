from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.http import HttpResponse
from django.template import Context, loader
from django.utils import timezone

from .forms import RegistrationForm
from .models import CustomUser

#-----------------------------------------------------------------------------

class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = CustomUser

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.slug = obj.email
        obj.save()
        template = loader.get_template('accounts/registration_done.html')

        return HttpResponse(template.render())

#-----------------------------------------------------------------------------

class AccountDetailView(DetailView):

    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()

        return context

    def account_detail(self, slug):
        account = get_object_or_404(CustomUser, slug)

        return render(request, 'accounts/customuser_detail.html', {'accounts': account})

#-----------------------------------------------------------------------------

class AccountUpdateView(DetailView):

    model = CustomUser
    fields = ['First Name', 'Last Name', 'ID']
    template_name_suffix = '_update_form'

    def get(self, slug, **kwargs):
        account = get_object_or_404(CustomUser, slug)

        return render(request, 'accounts/customuser_update_form.html', {'accounts': account})

    def get_object(self, queryset=None):
        return self.request.user

#-----------------------------------------------------------------------------
