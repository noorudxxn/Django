from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def employee_directory(request):

    employees = [
        {
            'name': 'John',
            'job_title': 'Python Developer',
            'salary': 35000,
            'is_full_time': True
        },
        {
            'name': 'David',
            'job_title': 'Web Designer',
            'salary': 25000,
            'is_full_time': False
        },
        {
            'name': 'Alex',
            'job_title': 'Software Engineer',
            'salary': 45000,
            'is_full_time': True
        }
    ]

    return render(request, 'employees.html', {'employees': employees})