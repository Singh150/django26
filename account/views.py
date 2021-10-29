from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):
    signupform=UserCreationForm(request.POST or None)
    if signupform.is_valid():
        signupform.save()
        username=signupform.cleaned_data.get('username')
        raw_password=signupform.cleaned_data.get('password1')
        user=authenticate(username=username, password=raw_password)
        login(request,user)
        return redirect('todolist')
    return render(request,'signup.html',{'form':signupform})
        
