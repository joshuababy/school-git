from django.shortcuts import render,HttpResponse,redirect
from.models import  *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def carriers(request):
    return render(request,'carriers.html')

def Admission(request):
    return render(request,'admission.html')

def viewstudent(request):
    # obj=Student.objects.filter(division='10')
    # obj=Student.objects.filter(admsn_no='10030')
    if request.user.is_authenticated:
        if request.session['usertype']=='admin':
            obj=Student.objects.all()
            return redirect(home)
        else:
            return render(request,'login.html',{'data':obj})
    else:
        return redirect(loginfn)
    

def loginfn(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        check=authenticate(request,username=username,password=password)
        if check:
            login(request,check)
            request.session['usertype']='admin'
            return redirect(home)
        else:
            return render(request,'login.html')

def addstudent(request):
    if request.method=='GET':
        nef=newstudent()
    # return HttpResponse("about us")
        return render(request,'addstd.html',{'data':nef})
    else:
        nef=newstudent(request.POST)
        if nef.is_valid():
            nef.save()
            return redirect(addstudent)
        else:
            return render(request,'addstd.html',{'data':nef})