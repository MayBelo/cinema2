from django.urls import path
from . import views
 
app_name = "movies"

urlpatterns = [
   path('', views.movies, name="movies"),
   path('search',views.find_movie,name="search"),
   path('<pk>/', views.movie_details, name="single"),
   path('login',views.loginPage,name="login"),
   path('logout',views.logout_user,name="logout"),
   path('register',views.register_user,name="register")

]
