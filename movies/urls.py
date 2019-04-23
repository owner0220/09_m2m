from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:movie_pk>', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/scores/new', views.movie_score_new, name='movie_score_new'),
    path('<int:movie_pk>/scores/<int:score_id>/delete', views.movie_score_delete, name='movie_score_delete'),
]
