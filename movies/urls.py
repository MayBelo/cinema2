from django.urls import path
from . import views
 
app_name = "movies"

urlpatterns = [
   path('', views.movies, name="movies"),
   path('search',views.find_movie,name="search"),
   path('show/<pk>/', views.movie_details, name="single"),
   path('login',views.loginPage,name="login"),
   path('logout',views.logout_user,name="logout"),
   path('register',views.register_user,name="register"),
   path('add_movie/',views.add_movie,name="addmovie"),
   path('delete_movie/<pk>',views.delete_movie,name="delete_movie"),
   path('add_movie_action/',views.add_movie_action,name="add_movie_action"),
   path('add_screening/',views.add_screening,name="addscreening"),
   path('add_screening_action/',views.add_screening_action,name="add_screening_action"),
   path('add_hall/',views.add_hall,name="addhall"),
   path('add_screening_action/',views.add_screening_action,name="add_hall_action"),
   path('tickets/<pk>/',views.buy_tickets,name='tickets')
   # path('cart',views.add_to_cart,name='cart' )

]
