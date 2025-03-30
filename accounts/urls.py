from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import EmailPasswordResetForm, passwordResetConfirmForm


app_name = 'accounts'  

urlpatterns = [
    path('signup/',  views.sign_up, name='signup'),
    path('signout/', views.sign_out, name='signout'),
    path('signin/', views.sign_in, name='signin'),
    path('change-password/', views.change_password, name='change_password'),

    # reset password
    path('reset-password/', auth_views.PasswordResetView.as_view(from_email = 'raflijf7@gmail.com'  ,template_name='reset_password/reset_password.html', email_template_name = 'reset_password/password_reset_email.html', success_url='/accounts/reset-password/done/', form_class = EmailPasswordResetForm ), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/reset_password_done.html'), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name = 'reset_password/reset_password_confirm.html', success_url='/accounts/reset-password-complete/' ,form_class = passwordResetConfirmForm  ), name="password_reset_confirm"),
    path("reset-password-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/reset_password_complete.html"), name="password_reset_complete"),

]
