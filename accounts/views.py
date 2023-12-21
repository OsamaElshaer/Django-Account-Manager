from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import login , authenticate
# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            userauth=authenticate(request , username=username , password=password)
            login(request , userauth)
            return redirect('/accounts/profile')
    else :
        form = SignupForm()


    context ={
        'form':form
    }
    return render( request , 'registration/signup.html' , context)