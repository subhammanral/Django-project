from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import logout,login, authenticate
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"This is SENT",
        "variable2":"This is GONE"
    }
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request, 'index.html',context)
    #return HttpResponse("THIS IS HOME PAGE 👍")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("THIS IS ABOUT PAGE 👍")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("THIS IS SERVICES PAGE 👍")

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials
        signin = authenticate(username=username, password=password)
        signin.save()
        messages.success(request, "SUCCESFULLY SIGNED IN !")
        if user is not None:
          # A backend authenticated the credentials
          signin(request,user)
          return redirect("/")

        else: 
          # No backend authenticated the credential
          return render(request, 'signin.html')
    return render(request, 'signin.html')
        
def signout(request):
    signout(request)
    return redirect("/signin")
 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "YOUR MESSAGE HAS BEEN SENT!")
    return render(request, 'contact.html')
    #return HttpResponse("THIS IS CONTACT PAGE 👍") 