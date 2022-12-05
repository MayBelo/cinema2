from django.forms import ModelForm
from movies.models import Movie,Hall,Screening
from django.contrib.auth.models import User

 
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'length', 'year' , 'image' , 'age_restrictions']
 

class HallForm(ModelForm):
    class Meta:
        model = Hall 
        fields = ['hall_number','type','seats','price']

class Screening(): 
    class Meta:     
        model = Screening
        fildes = "__all__"