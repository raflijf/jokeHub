from django import forms

class contact_form(forms.Form) : 
    email = forms.EmailField(
        widget=forms.TextInput(attrs= {
            'class' : 'form-control',
            'placeholder' : 'masukkan email anda'
        }),
        required=False
    )
    pesan = forms.CharField(
        max_length=None, 
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control bg-slate-400',
                'placeholder' : 'Masukkan pesan anda',
                'rows' : 5,
                'cols' : 50
            }
        ),
        required=False

    
    )