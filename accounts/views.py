from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render 
from .forms import *
from django.contrib.auth import login , authenticate
from . models import Profile
from django.urls import reverse

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

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except User.DoesNotExist:
        raise HttpResponseNotFound

    return render(request , 'profile/profile.html' , {'profile':profile})


def profile_edit(request):
    profile=Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform=UserForm(request.POST , instance= request.user)
        profileform=ProfileForm(request.POST , instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profile=profileform.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)
    context={
        'userform':userform,
        'profileform':profileform
    }
    return render(request , 'profile/profileedit.html',context)


 