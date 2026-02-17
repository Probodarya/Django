from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.student_home, name='student_home'),  
    path('profile', views.student_profile, name="profile"),
    path('courses', views.student_courses, name="course"),
    path('grades', views.student_grades, name="grade"),
]