
#
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
import requests
from .models import Movie


class MovieListView(ListView):
    model = Movie

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title']
    success_url = '/movie_list'


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/movie_list'


class MovieDetailView(DetailView):
    model = Movie
