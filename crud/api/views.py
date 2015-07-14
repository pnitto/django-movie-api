from django.shortcuts import render

from crud.models import Movie
import requests

# wanting to get 1 movie
def one_movie(request,movie_id):
    if request.method == "GET":
        movie = Movie.objects.get(pk=movie_id)
        return requests.get('http://127.0.0.1:8000/movie_list/{}/'.format(movie_id)).json()
# Not quite sure if I need to use .json() for this data
#
def all_movies(request):
    if request.method == "GET":
        all_movies = Movie.objects.all()
        return requests.get('http://127.0.0.1:8000/movie_list/').json()

def create_movie(request):
    if request.method == "POST":
        created_movie = Movie.objects.create(title="Batman Begins")
        return requests.get('http://127.0.0.1:8000/movie_form/').json()

def delete_movie(request, movie_id):
    if request.method == "POST":
        deleted_movie = Movie



# create a movie
#def create_movie(request, movie_id):
#    if request.method == 'POST':
 #       new_movie = Movie.objects.create(title="The Dark Knight")
  #      return render(request, 'movie_form.html')