from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User ,auth
from django.contrib import messages
import numpy as np
from statistics import mode


def index(request):
    return render(request, 'Home.html')

def Login(request):
    return render(request, 'Login.html')

def SignUp(request):
    return render(request, 'Signup.html')

def Submit(request):
    if request.method=="POST":
        # Get the post parameters
        FName=request.POST['FName']
        LName=request.POST['LName']
        Email=request.POST['Email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['Cpassword']


        # check for errorneous input
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            else:
                myuser = User.objects.create_user(username, Email, password)
                myuser.first_name= FName
                myuser.last_name= LName
                myuser.save()
                messages.info(request, "User Created")
        else:
            messages.info(request, 'Password not matching')
            return redirect('/SignUp')
        return redirect('/SignUp')
    else:
        return render(request, 'Signup.html')

def ULogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/user')
        else:
            messages.info(request, "Invalid Credential")
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

def user(request):
    return render(request, 'user.html')

def calc(request):
    if request.method=="POST":
        # Get the post parameters
        one= request.POST['one']

        two = request.POST['two']
        three=request.POST['three']
        four=request.POST['four']
        five=request.POST['five']
        six=request.POST['six']
        seven=request.POST['seven']
        eight=request.POST['eight']
        nine=request.POST['nine']
        List = [one,two,three,four,five,six,seven,eight,nine]
        L1=[]
        for i in List:
            try:
                k = int(i)
                L1.append(k)
                #messages.info(request, one)
            except:
                messages.info(request, "Please enter valid number")
                break
            

        if len(L1) == len(List):
            #messages.info(request, L1)
            y = np.median(L1)
            x = np.mean(L1)
            z = mode(L1)
            return render(request, 'user.html', {'Result_Mean':x, 'Result_Meadian':y, 'Result_Mode':z})
        else:
           return render(request, 'user.html')     
    else:
        return render(request, 'user.html')
        

