from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordChangeDoneView

from .views import UserLoginView, UserRegistrationView, EmailVerificanionView

app_name = 'users'

urlpatterns = [
    path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificanionView.as_view(), name='email_verification'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name="users/password_reset_form.html"), name='password_reset_form'),
    path('password_reset_done/', PasswordChangeDoneView.as_view(), name='password_reset_done'),
]