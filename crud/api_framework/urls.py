
from django.conf.urls import url
from django.http import HttpResponse

from .views import MovieListCreateAPIView, MovieDetailAPIView, hello




urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^movie/$', MovieListCreateAPIView.as_view(), name="movie_list_create_api_view"),
    url(r'^movie/(?P<pk>\d+)/$', MovieDetailAPIView.as_view(), name="movie_detail_api_view"),
    ]