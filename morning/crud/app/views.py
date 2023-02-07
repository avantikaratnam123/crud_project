from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from . models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")


def table(request):
    return render(request,"table.html")

def registration(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        DOB=request.POST['DOB']
        password=make_password(request.POST['password'])
        if  User.objects.filter(email=email).exists():
            messages.error(request,"email already exists")
        elif User.objects.filter(contact=contact).exists():
            messages.error(request,"contact already exists")
        else:
            User.objects.create(name=name,email=email,contact=contact,DOB=DOB,password=password)

        return redirect('/login/')   

def table(request):
    data = User.objects.all()
    return render(request,"table.html",{"data":data})

def Login_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        User_password = request.POST['password']
        if User.objects.filter(email=email).exists():
             obj =User.objects.get(email=email)
             password =obj.password
             if check_password(User_password,password):
                return redirect('/welcome/')
                # return render(request,'welcome.html')
             else:
                return HttpResponse('password incorrect')
        else:
             return HttpResponse('email is not registered')
             # return render(request,'welcome.html')



#create edit button

def update_view(request,uid):
    res=User.objects.get(id=uid)
    return render(request,'update.html',{'person':res})


#USE UPDATE DATA
def update_form_data(request):
    if request.method == "POST":
        uid = request.POST['uid']
        name =request.POST['name']
        email =request.POST['email']
        DOB=request.POST['DOB']
        contact =request.POST['contact']
        User.objects.filter(id=uid).update(name=name,email=email,DOB=DOB,contact=contact)
        return redirect('/table/')
            

def welcome(request):
    return render(request,"welcome.html")

def delete(request,pk):
    use = User.objects.filter(id=pk).delete()
    return redirect('/table/')




