from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
# Create your views here.

def home(requests):
    return render(requests,"home.html")

def Login(requests):
    if requests.method == 'POST':
        name = requests.POST['username']
        password= requests.POST['password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            login(requests,user)
            return redirect("/")
        else:
            messages.info(requests,"Invalid Email/Password")
            return render(requests,"signin.html")
    else:
        return render(requests,"signin.html")

def Register(requests):
  if requests.method == 'POST':
    username = requests.POST['username']
    email = requests.POST['email']
    password=  requests.POST['password']
    confirmPassword = requests.POST['confirm-password']
    # course=requests.POST['course']
    if password==confirmPassword:
        print(username)
        if User.objects.filter(username=username).exists():
            messages.info(requests,"Username already exists")
            return render(requests,"signup.html")
        elif User.objects.filter(email=email).exists():
            messages.info(requests,"Email already exists")
            return render(requests,"signup.html")
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            login(requests,user)
            print("User created")
            return redirect('/')
    else:
        messages.info(requests,"Password dont match")
        return render(requests,"signup.html")
  else:
        return render(requests,"signup.html")
        
def Logout(requests):
    auth.logout(requests)
    return redirect("/")
