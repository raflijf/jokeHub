from django import forms
from .models import Post, Comment

class postForm(forms.ModelForm) :
    class Meta :
        fields = ['content']
        model = Post

        widgets = {
            'content' : forms.Textarea(
                attrs={
                    'id' : 'contentPost',
                    'placeholder' : 'Masukkan jokes anda disini'
                }
            )
        }

class commentForm(forms.ModelForm) :
    class Meta :
        fields = ['content']
        model = Comment

        widgets = {
            'content' : forms.Textarea(
                attrs={
                    'id' : 'Comment',
                    'placeholder' : 'Berikan komentar anda'
                }
            )
        }

class searchForm(forms.Form) :
    search = forms.CharField(max_length=200, required=False, widget=forms.TextInput(
        attrs={
            'type' : 'search',
            'placeholder' : 'Cari',
            'autocomplete' : "off"
        }
    ))
     