from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm


user = get_user_model()
class registerForm(UserCreationForm) : 
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password'
            }
        ),
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Konfirmasi password'
            }
        ),
        required=False
    )
    username = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={
                'placeholder' : 'Username',
                'onkeydown' : 'return event.key !== ' ';'
                
        }),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email'
            }
        )
    )

    class Meta : 
        model = user
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={
                'placeholder' : 'Username',
                
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder' : 'Email' ,
                
            }),
        }


class signinForm(forms.Form) :
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email'
            }
        ),
        required=False

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password'
            }
        ),
        required=False,
    )

class changePasswordForm(PasswordChangeForm) : 
    def __init__(self,  *args, **kwargs):
        super().__init__( *args, **kwargs)\

        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password lama',
                
            }
        )
        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password baru'
            }
        )
        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Konfirmasi password baru'
            }
        )

    class Meta : 
        model = user
        fields = ['old_password', 'new_password1', 'new_password2']

    
class EmailPasswordResetForm(PasswordResetForm) : 
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email',
                'id' : 'email'
            }
        ),
        required=False
    )

class passwordResetConfirmForm(SetPasswordForm) : 
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'placeholder' : 'Password baru'
        })
        self.fields['new_password2'].widget.attrs.update({
            'placeholder' : 'Konfirmasi password baru'
        })