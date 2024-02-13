from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateUserForm, EditUserForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        id = request.POST["username"]
        pw = request.POST["password"]
        user = authenticate(username=id, password=pw)
        if user is not None:
            login(request, user)
            return redirect("post-list")
        else:
            return redirect("user-login")
    else:
        form = LoginForm()
        return render(request, "users/user_login.html", {"form": form})



def user_logout(request):
    logout(request)
    return redirect("post-list")



def user_create(request):
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            new_user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name)
            login(request, new_user)
            return redirect('post-list')
    else :
        form = CreateUserForm()
        return render(request,"users/user_create.html",{"form":form})
    
    

def user_pw_edit(request):
    # user = User.objects.get(id = user_pk)
    if request.method == "POST":
        user_form = PasswordChangeForm(request.user, request.POST)        
        if user_form.is_valid():
            user_form.save()
            context = {'form':user_form}
            # context = {'user':user,'form':user_form}
            return redirect("user-pw-change")
    else:
        form = PasswordChangeForm(request.user)
        context = {'form':form}
        # context = {'user':user,'form':form}
        return render(request,"users/user_pw_change.html",context)
    


def user_edit(request,user_id):
    user = User.objects.get(id = user_id)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('post-list')
        
    else : 
        form = EditUserForm(instance=user)
        return render(request,'users/user_edit.html',{'form':form})
    