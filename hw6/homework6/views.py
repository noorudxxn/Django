from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Contact

def contact(request):

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )

        return render(request, 'contact.html', {
            'name': full_name
        })

    return render(request, 'contact.html')