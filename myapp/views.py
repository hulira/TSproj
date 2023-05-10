from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from myapp.models import Staff_Details
from . import views
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from tsproj import settings
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,"myapp/index.html")
    

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname  =request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
#Validation
        if Staff_Details.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if Staff_Details.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username=username, password=pass1, email=email,first_name=fname,last_name=lname)
      

       # myuser = Staff_Details.objects.create(username, email, pass1)
       
       # myuser = Staff_Details(username=username,email=email,fname=fname,lname=lname)
       
       
       
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.password = pass1
        myuser.save()   

        messages.success(request, "Your account has been created successfully ")
       #Email message

        # subject = "Welcome to Time sheet Management System!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Time sheet Portal!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAdmin"        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
              
        return redirect('signin')
    else:
        return render(request,"myapp/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
       
        user = authenticate(request, username=username, password=pass1)
       
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "myapp/index.html", {'fname': fname})
            # messages.success("Login successful")
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    else:
         return render(request,"myapp/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')
   