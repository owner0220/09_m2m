from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Genre,Movie,Score
from .forms import *
from django.views.decorators.http import require_POST

# Create your views here.
def list(request):
    movielist = Movie.objects.all()
    return render(request, 'movies/list.html',{'movielist':movielist})
    
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie,id=movie_pk)
    score_form = ScoreForm()
    return render(request, 'movies/movie_detail.html',{'movie':movie,'score_form':score_form})
    
@login_required
@require_POST
def movie_score_new(request,movie_pk):
    score_form = ScoreForm(request.POST)
    if score_form.is_valid():
        score = score_form.save(commit=False)
        score.user = request.user
        score.movie = Movie.objects.get(id=movie_pk)
        score.save()
        return redirect("movies:movie_detail",movie_pk)
    else:
        return redirect("movies:list")

@login_required
def movie_score_delete(request,movie_pk,score_id):
    score = Score.objects.get(id=score_id)
    if score.user == request.user:
        score.delete()
    return redirect("movies:movie_detail", movie_pk)