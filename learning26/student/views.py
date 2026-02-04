from django.shortcuts import render

# Create your views here.
def student_home(request):
    return render(request, 'student\student_home.html')

def student_profile(request):
    students_name = ['Alice', 'Bob', 'Charlie']
    return render(request, 'student\student_profile.html', {'students_name': students_name})

def student_courses(request):
    student_courses = ['Math', 'Science', 'History']    
    return render(request, 'student\student_courses.html', {'student_courses': student_courses})

def student_grades(request):
    student_grades = {'Math': 'A', 'Science': 'B+', 'History': 'A-'}    
    return render(request, 'student\student_grades.html', {'student_grades': student_grades})