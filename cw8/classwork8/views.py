from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'classwork8/home.html')

def about(request):
    return render(request, 'classwork8/about.html')