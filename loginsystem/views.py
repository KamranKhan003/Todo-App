from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from .forms import LoginForm, UserPasswordChangeform, UserPasswordResetForm, UserSetPasswordForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Login View
class UserLoginView(LoginView):

    authentication_form = LoginForm
    template_name = 'loginsystem/login.html'

# Password Reset View
class UserPasswordResetView(PasswordResetView):

    form_class = UserPasswordResetForm
    template_name = 'loginsystem/password_reset.html'

# Password Reset Done View
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'loginsystem/password_reset_done.html'

# Password Reset Confirm View
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = 'loginsystem/password_reset_confrim.html'
    success_url = '/accounts/login/'


# Profile View
@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):

    template_name = 'todo/home.html'

# Password Change Form
class UserPasswordChangeView(PasswordChangeView):

    form_class = UserPasswordChangeform
    template_name = 'loginsystem/password_change.html'
    success_url = '/accounts/profile/'

# Logout view
class UserLogoutView(LogoutView):
    
    next_page = '/'