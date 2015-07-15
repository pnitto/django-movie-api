from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
from movie.models import Movie


def hello(request):
    return HttpResponse("Hello World")



class MovieSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        return reverse("movie_detail_api_view", kwargs={"pk": obj.pk})


    class Meta:
        model = Movie
        fields = [ "id","title", "url",]


class MovieListCreateAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

