from django.http import HttpResponse
from django.shortcuts import render

def Aboutus(request):
    return render(request, 'aboutus.html')

def Contactus(request):
    return render(request, 'contactus.html')

def home(request):
    return render(request, 'home.html')