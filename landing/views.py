from django.shortcuts import render, redirect
from .forms import contact_form
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def index(request) : 
    if request.user.is_authenticated : 
        return redirect('hubspace:homepage')

    context = {
        'title' : 'Beranda'
    }
    return render(request, 'landing/index.html', context)

def about(request) :
    context = {
        'title' : 'Tentang kami' 
    }
    return render(request, 'landing/about.html', context)

def contact(request) : 
    form = contact_form(request.POST or None)
    if request.method == 'POST' : 
        if form.is_valid() : 
            send_mail(
                subject=f'Pesan masuk dari {form.cleaned_data.get('email')}',
                message=f'{form.cleaned_data.get('pesan')}',
                from_email=form.cleaned_data.get('email'),
                recipient_list=['raflijf7@gmail.com']
            )
            messages.success(request, 'pesan berhasil dikirim')
            return redirect('landing:contact')
        else :
            print('dak biso')
            
    context = {
        'title' : 'kontak',
        'form' : form
    }
    return render(request, 'landing/contact.html', context)