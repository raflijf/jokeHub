from django import template

register = template.Library()

@register.simple_tag
def translate_error(error) : 
    listError = {
        'Your old password was entered incorrectly. Please enter it again.' : 'Password salah',
        "The two password fields didn’t match." : 'Kedua password baru tidak sama',
        'This password is too common.' : 'Password ini terlalu umum, coba masukkan password lain'
    }
    return listError.get(error, '')