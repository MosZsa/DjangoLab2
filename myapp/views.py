from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def PageO(request, param):
    return render(request, 'Page1.html', {'param': param })

def PageT(request, param1, param2):
    return render(request, 'Page2.html', {'param1': param1, 'param2': param2})
