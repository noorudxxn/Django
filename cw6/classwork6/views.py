from django.shortcuts import render
from .models import Movie

def add_movie(request):

    message = ""

    if request.method == "POST":

        movie_name = request.POST.get('movie_name')
        release_year = request.POST.get('release_year')

        movie = Movie(
            movie_name=movie_name,
            release_year=release_year
        )

        movie.save()

        message = f"Movie saved: {movie_name} ({release_year})"

    return render(request, 'movie.html', {'message': message})