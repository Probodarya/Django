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

def team(request):
    players = ["virat kohli","rohit sharma","jasprit bumrah"]
    data = { 'team_name':'gujrat titans','captain':'hardik pandya','trophy_count':'6','players': players }

    return render(request, 'team.html', data)

def student(request):
    subject = ["C","C++","Java","Python"]
    data = { 'student_name':'rahul','age':20,'subjects': subject }
    return render(request, 'student.html', data)