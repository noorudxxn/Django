from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Signup
def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'classwork11/signup.html')


# Login
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('visit_counter')

    return render(request, 'classwork11/login.html')


# Visit Counter
@login_required
def visit_counter(request):

    count = request.session.get('visit_count', 0)

    count += 1

    request.session['visit_count'] = count

    return render(request, 'classwork11/visit_counter.html', {
        'count': count
    })


# Logout
def user_logout(request):

    logout(request)

    return redirect('login')