from django.http import HttpResponse
from django.shortcuts import render

def Aboutus(request):
    return render(request, 'aboutus.html')

def Contactus(request):
    return render(request, 'contactus.html')

def home(request):
    return render(request, 'home.html')

def movies(request):
    return render(request, 'movies.html')

def shows(request):
    return render(request, 'shows.html')

def news(request):
    return render(request, 'news.html')

def recepies(request):
    ingredient = ["poori","masala","pani"]
    data = { 'name': 'panipoori','price': 50, 'ingredients': ingredient }
    return render(request, 'recepies.html', data)