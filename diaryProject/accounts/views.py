from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request)  :
    if request.method == "POST" :
        new_user = User.objects.create_user(username=request.POST['userName'], password=request.POST['userPassword'])
        auth.login(request, new_user)
        print("회원가입 성공")
        return redirect('home')
    return render(request, 'join.html')

def login(request) :
    if request.method == "POST" :
        username = request.POST["userName"]
        password = request.POST["userPassword"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None :
            auth.login(request, user)
            print("로그인 성공")
            return redirect('home')
        else :
            return render(request, 'bad_login.html')
    else :
        return render(request, 'login.html')
    
def logout(request) :
    auth.logout(request)
    return redirect('home')