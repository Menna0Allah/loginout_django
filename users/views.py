from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "wronge username or password dude but if you do not have an account, create one ;)")
            return render(request, 'login.html')  
        
    return render(request, 'login.html')

   
    
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
        except:
            messages.error(request, 'this username is taken already !')
            return render(request, 'register.html')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    # if not request.user.is_authenticated:  
    #     messages.error(request, "dude you must login first if you want to do to home :)")
    #     return redirect('login') 
    return render(request, 'home.html')
