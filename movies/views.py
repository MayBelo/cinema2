from django.shortcuts import render, redirect
from movies.models import Movie,Hall,Screening
from movies.forms import MovieForm,HallForm,ScreeningForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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


def movies(request):
    movie_list = Movie.objects.all()
    context={
        'movie_list' : movie_list
    }
    return render(request,'movies.html',context)


def add_movie(request):
    context= {
        'movieform':MovieForm(),
    }
    return render(request,'addmovie.html',context)

def add_screening(request):
    context= {
        'screeningform':ScreeningForm(),
    }
    return render(request,'addscreening.html',context)

def add_hall(request):
    context= {
        'hallform':HallForm(),
    }
    return render(request,'addhall.html',context)

def delete_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect('movies:movies')


def add_screening_action(request):
    if request.method == "POST":
        screeningform = ScreeningForm(request.POST, request.FILES)
        if screeningform.is_valid():
                screeningform.instance.tickets_left = screeningform.instance.hall_id.seats
                screeningform.save()
                messages.success(request,'screening added successfuly')
                return redirect('movies:addscreening')
    else:
        context= {
            'screeningform': screeningform,
        }
        return render(request,'addscreening.html',context)

def add_movie_action(request):
    if request.method == "POST":
        movieform = MovieForm(request.POST, request.FILES)
        if movieform.is_valid():
            movieform.save()
            messages.success(request,'movie added successfuly')
            return redirect('movies:addmovie')
    else:
        context= {
            'movieform': movieform,
        }
        return render(request,'addmovie.html',context)

def add_hall_action(request):
    if request.method == "POST":
        hallform = HallForm(request.POST, request.FILES)
        if hallform.is_valid():
            hallform.save()
            messages.success(request,'hall added successfuly')
            return redirect('movies:addhall')
    else:
        context= {
            'hallform': hallform,
        }
        return render(request,'addhall.html',context)
   
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


def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    screenings_time = Screening.objects.filter(movie_id=movie.id,screening_time__gt=timezone.now())
    return render(request,'movie_details.html',{'screening_time':screenings_time,'movie':movie})


def buy_tickets(request, pk): # this pk should be the screening pk
    seats = int(request.POST.get('number_of_tickets'))
    scr1 = Screening.objects.get(id=pk)
    scr1.tickets_left = scr1.tickets_left - seats
    scr1.save()
    price = scr1.hall_id.price
    payment = int(seats*price)
    return render(request,'tickets.html',{'payment':payment,'screnning':scr1,'seats':seats})


def show_halls_vip(request):
    hall_type = request.GET.get('type')
    halls_list = Hall.objects.filter(type__contains=hall_type)
    context = {
        'halls_list' : halls_list,
        'hall_type': hall_type
    }
    return render(request,'vip.html',context=context,)


def show_halls_3d(request):
    hall_type = request.GET.get('type')
    halls_list = Hall.objects.filter(type__contains=hall_type)
    context = {
        'halls_list' : halls_list,
        'hall_type': hall_type
    }
    return render(request,'3d.html',context=context,)



