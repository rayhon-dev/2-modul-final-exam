from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm, UserProfileForm
from django.views import View
from .models import UserProfile
from django.contrib.auth import logout


class UserLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('username')  # Formdan username o‘rniga email olinadi
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=email, password=password)  # username o‘rniga email ishlatiladi
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile-update.html'
    success_url = reverse_lazy('users:update_profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return render(request, 'users/logout.html')