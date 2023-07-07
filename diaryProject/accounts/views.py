from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request)  :
    if request.method == "POST" :
        username = request.POST['userName']
        password = password=request.POST['userPassword']
        
        # username이 같은게 있으면 bad_join.html
        if User.objects.filter(username=username).exists():
            return render(request, 'bad_join.html')
        
        user = auth.authenticate(request, username=username, password=password)
        # 같은 user가 없을 때 -> 성공
        if user is None :
            new_user = User.objects.create_user(username=username, password=password)
            auth.login(request, new_user)
            print("회원가입 성공")
            return redirect('home') 
        else :
            return render(request, 'bad_join.html')
    
    else :
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