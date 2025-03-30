from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import registerForm, signinForm, changePasswordForm
# Create your views here.
def sign_up(request) : 
    if request.user.is_authenticated : 
        return redirect('hubspace:homepage')
    
    register_form = registerForm(request.POST or None)
    if request.method == 'POST' : 
        if register_form.is_valid() : 
            user =  register_form.save()
            login(request, user)
            return redirect('hubspace:homepage')
        else : 
            print(register_form.errors)
            redirect('accounts:signup')
    else : 
        register_form = registerForm()

    context = {
        'title' : 'Sign up',
        'form' : register_form
    }

    return render(request, 'accounts/sign_up.html', context)

def sign_in(request) :
    if request.user.is_authenticated : 
        return redirect('hubspace:homepage')
    
    form = signinForm(request.POST or None) 
    context = {
        'title' : 'sign in',
        'form' : form
    }

    if request.method == 'POST' : 
        if form.is_valid() : 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user_auth = authenticate(email = email, password = password)
            if user_auth is not None : 
                login(request, user_auth)
                print('biso nah')
                print(user_auth)
                return redirect('hubspace:homepage')
            else :
                print('dak biso')
                print(user_auth)
                context['user_auth'] = True
    return render(request, 'accounts/sign_in.html', context)

def sign_out(request) : 
    logout(request)
    return redirect('landing:home')


def change_password(request) : 
    form = changePasswordForm(data = request.POST, user = request.user)
    if request.method == 'POST' :             
        if form.is_valid() : 
            form.save()
            return redirect('accounts:signin')
        else : 
            print(form.errors)

    context = {
        'titile' : 'ubah password',
        'fields' : form,
    }
    return render(request, 'accounts/change_password.html', context)


