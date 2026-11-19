from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


# Display students and search
def home(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    return render(request, 'homework10/home.html', {
        'students': students,
        'search': search
    })


# Add student
def add_student(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        student_class = request.POST.get('student_class')
        age = request.POST.get('age')

        Student.objects.create(
            name=name,
            student_class=student_class,
            age=age
        )

        return redirect('home')

    return render(request, 'homework10/add_student.html')


# Edit student
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.age = request.POST.get('age')

        student.save()

        return redirect('home')

    return render(request, 'homework10/edit_student.html', {
        'student': student
    })


# Delete student
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('home')