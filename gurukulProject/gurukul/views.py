from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth import authenticate
from .models import User
class MyView(TemplateView):
    template_name = 'pages/my_view.html'
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")

def user_register(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        pswd=request.POST.get("password")
        phone_no=request.POST.get("phone_no")
        user=User.objects.create(name=name,email=email,password=pswd,phone_no=phone_no)
        user.save()
        return render(request,"register.html")
    else:
        return render(request,"login.html")

def user_login(request):
    if request.method == 'POST':
        import pdb;
        pdb.set_trace()
        email=request.POST.get("email")
        pswd=request.POST.get("password")
        user=authenticate(email=email,password=pswd)
        if user:
            login(request,user)
            return render(request,"login.html")
        else:
            return render(request,"register.html")
    else:
        return render(request,"register.html")

