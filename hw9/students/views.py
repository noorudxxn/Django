from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def student_list(request, message):

    students = ['Noor', 'Rahul', 'Arun', 'Anu']

    return render(request, 'students/student_list.html', {
        'students': students,
        'message': message
    })