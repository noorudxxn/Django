from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')