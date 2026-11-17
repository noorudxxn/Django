from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def teacher_list(request, message):

    teachers = ['John', 'Smith', 'David', 'Mary']

    return render(request, 'teachers/teacher_list.html', {
        'teachers': teachers,
        'message': message
    })