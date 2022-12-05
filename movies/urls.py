from django.urls import path
from . import views
 
app_name = "movies"

urlpatterns = [
   path('', views.movies, name="movies"),
   path('search',views.find_movie,name="search"),
   path('<pk>/', views.movie_details, name="single"),
]
