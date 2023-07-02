from django.shortcuts import render

def home(request): 
	return render(request, "main.html") # index.html 렌더링

def mainlist(request) : 
    return render(request, "mainList.html")