from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import LoginForm
def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'fromresult.html',{
                 'email': form['email'].value,
             })
    else:
        form = LoginForm()
    return render(request,'formslogin.html',{'form':form})