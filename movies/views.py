from django.shortcuts import render, redirect
from movies.models import Movie,Hall
from movies.forms import MovieForm

def movies(request):
    movie_list = Movie.objects.all()
    context={
        'movie_list' : movie_list
    }
    return render(request,'movies.html',context)

def add_movie(request):
    context = {
        'movie_form' : MovieForm(),
    }
    return render(request,'addmovie.html', context)

def add_movie_action(request):
    if request.method == "POST":
        movieform = MovieForm(request.POST, request.FILES)
        if movieform.is_valid():
            movieform.save()
            return redirect('movies:movies')
    else:
        context = {
            'movieform': movieform,
        }
        return render(request, 'addmovie.html', context)
        
def find_movie(request):
    my_search1 = request.GET.get('my_search')
    movie_list = Movie.objects.filter(name__icontains=my_search1)
    context = {
        'movie_list' : movie_list,
    }
    return render(request, 'movies.html', context=context)

def show_movie_by_genre(request):
    genre_search = request.GET.get('genre')
    movie_list = Movie.objects.filter(genre__contains=genre_search)
    context = {
        'movie_list' : movie_list,
    }
    return render(request, 'movies.html', context=context)


def show_halls_by_type(request):
    hall_type = request.GET.get('type')
    halls_list = Hall.objects.filter(type__contains=hall_type)
    context = {
        'halls_list' : halls_list
    }
    return render(request,'halls.html',context=context)


# def show_screening(request):

def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie_details.html', {'movie':movie})







# def buy_ticket(request): 