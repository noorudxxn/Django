from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import RegistrationForm

def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['full_name']

            return render(request, 'loginresult.html', {'name': name})

    else:
        form = RegistrationForm()

    return render(request, 'loginpage.html', {'form': form})