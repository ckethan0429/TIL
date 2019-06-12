from django.shortcuts import render,redirect
from .models import Genre, Movie, Score
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    print(movies)
    #print(movies)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.audience = format(movie.audience, ',')
    scores = movie.score_set.order_by('-pk')
    context = {
        'movie': movie,
        'scores': scores,
    }
    return render(request, 'movies/detail.html', context)


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')

    else:
        return redirect('movies:detail', movie_pk)


def scores_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        score = request.POST.get('score')
        # 댓글 생성 및 저장
        value = Score(movie=movie, content=content, score=score)
        value.save()

        return redirect('movies:detail', movie_pk)

