from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home_page(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        mail=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse('oops!! password doses not match')
        try:
            my_user=User.objects.create_user(uname,mail,pass1)
            print(uname,mail,pass1,pass2)
            my_user.save()
            # return HttpResponse("user has been created succesfully")
            return redirect('login')

        except IntegrityError:
            return HttpResponse("Username already exists, please choose a different username") 
    else:
        return render(request,'signup.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse(' oops !!! username or password is incorrect....')

    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

    