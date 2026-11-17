from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):

    students = ['Noor', 'Rahul', 'Arun', 'Anu']

    return render(request, 'home.html', {'students': students})


def result(request, name):

    results = {
        'Noor': 95,
        'Rahul': 85,
        'Arun': 90,
        'Anu': 88
    }

    mark = results.get(name)

    return render(request, 'result.html', {
        'name': name,
        'mark': mark
    })