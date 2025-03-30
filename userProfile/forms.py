from django import forms
from accounts.models import User

class userForm(forms.ModelForm) : 
    class Meta : 
        model = User
        fields = ['bio', 'username', 'email', 'full_name', 'profile_image']

        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'placeholder' : 'Username'
                }
            ),
            'bio' : forms.Textarea(
                attrs = {
                    'placeholder' : 'Bio',
                    'rows' : '3'
                    
                }
            ),
            'email' : forms.EmailInput(
                attrs= {
                    'placeholder' : 'Email'
                }
            ),
            'full_name' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Nama lengkap'
                }
            )
            
        }
