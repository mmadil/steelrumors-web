from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from .models import User
from .forms import UserProfileForm


class UserProfileDetailView(DetailView):
    context_object_name = 'userinfo'
    template_name = 'users/user_detail.html'
    model = User

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return user

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['userprofile'] = user
        return context


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/edit_profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})
