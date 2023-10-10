from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import RegisterForm

# Create your views here.


def loginUser(request):

    # if request.user.is_authenticated:
    #     return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request,'username does not exist..')


        # this will check username match the password if it is it return a instance else none
        user = authenticate(request, username=username, password=password )

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request,'username or password is incorrect..')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request,'user was loged out..')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request,user)
            return redirect('projects')

        else:
            messages.error(request,'An error has occurred during registration..')

    context = {}
    return render(request, 'users/login_register.html',{'page':page, 'form':form})


def myAccount(request):
    user = request.user
    projects = user.projects_set.all()

    context = {'user':user,'projects':projects}
    return render(request,'users/my_account.html',context)
