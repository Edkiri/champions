"""User views."""

# Django
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, DetailView, UpdateView

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from users.forms import SignupForm

# Models
from users.models import User, Profile


class SignupView(FormView):

	template_name = 'users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		"""Save form data"""
		form.save()
		return super().form_valid(form)


class LoginView(auth_views.LoginView):

	template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
	"""Logout user."""


class UserDetailView(LoginRequiredMixin, DetailView):

	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()
	context_object_name = 'user'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'users/update_profile.html'
	model = Profile
	fields = ['biography', 'picture']

	def get_object(self):
		"""Return user's profile"""
		return self.request.user.profile

	def get_success_url(self):
		"""return to user's profile"""
		username = self.object.user.username
		return reverse('users:detail', kwargs={'username': username})
