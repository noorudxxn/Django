from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def student_list(request):

    students = [
        {'name': 'Ajay', 'grade': 'A', 'passed': True},
        {'name': 'Vineeth', 'grade': 'B', 'passed': True},
        {'name': 'Rahul', 'grade': 'C', 'passed': False},
        {'name': 'Arun', 'grade': 'A+', 'passed': True},
        {'name': 'Manu', 'grade': 'D', 'passed': False}
    ]

    return render(request, 'students.html', {'students': students})