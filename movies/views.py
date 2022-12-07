from django.shortcuts import render, redirect
from movies.models import Movie,Hall,Screening
from movies.forms import MovieForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.utils import timezone

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('movies:movies')

    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
            return render(request,'login.html',{})

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('movies:movies')
        else:
            messages.error(request, 'Username or password does not exists')


    return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    return render(request,'login.html',{})

def register_user(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request,'register.html',{'form':form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:movies')
        messages.error(request,'Error')
        return render(request,'register.html',{'form':form})

# @login_required(login_url='login')
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

# @login_required(login_url='login')     
def find_movie(request):
    my_search1 = request.GET.get('my_search')
    movie_list = Movie.objects.filter(name__icontains=my_search1)
    context = {
        'movie_list' : movie_list,
    }
    return render(request, 'movies.html', context=context)

# @login_required(login_url='login')
def show_movie_by_genre(request):
    genre_search = request.GET.get('genre')
    movie_list = Movie.objects.filter(genre__contains=genre_search)
    context = {
        'movie_list' : movie_list,
    }
    return render(request, 'movies.html', context=context)

# @login_required(login_url='login')
def show_halls_by_type(request):
    hall_type = request.GET.get('type')
    halls_list = Hall.objects.filter(type__contains=hall_type)
    context = {
        'halls_list' : halls_list
    }
    return render(request,'halls.html',context=context)


# @login_required(login_url='login')
def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    screenings_time = Screening.objects.all()
    now = timezone.now() 
    for screening in screenings_time:
        if screening.screening_time <= now:
            screening.delete()
            return render(request,'movie_details.html',{'movie':movie})
        else:
            return render(request,'movie_details.html',{'screening_time':screenings_time,'movie':movie})


# def show_screening(request):
#     screenings_time = Screening.objects.all()
#     for screening in screenings_time:
#         if screening.screening_time <= datetime.datetime.now():
#             screening.delete()
#         else:
#             return (request,'movie_details.html',{'screening_time':screenings_time})
    



# def tickets_left(request):
# def buy_ticket(request): 
# def show_screening(request):
# def add_screenung(request):
# def add_hall(request):
# def delete_screening(request):
# def delete_movie(request):
# def delete_hall(movie):