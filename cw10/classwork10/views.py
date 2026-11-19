from django.shortcuts import render

# Create your views here.


# Display books
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Book


# Home page - Display books
def home(request):

    books = Book.objects.all().order_by('id')

    paginator = Paginator(books, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'classwork10/home.html', {
        'page_obj': page_obj
    })


# Add a new book
def add_book(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')

        Book.objects.create(
            title=title,
            author=author,
            year=year
        )

        return redirect('home')

    return render(request, 'classwork10/add_book.html')


# Edit book details
def edit_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':

        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.year = request.POST.get('year')

        book.save()

        return redirect('home')

    return render(request, 'classwork10/edit_book.html', {
        'book': book
    })


# Delete a book
def delete_book(request, id):

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect('home')