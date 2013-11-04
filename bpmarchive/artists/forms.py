__author__ = 'Kevin'
from .models import Artist
from django.forms import ModelForm
from django.forms import forms


#class ArtistForm(ModelForm):
#class ArtistForm(forms.form):
class ArtistForm(forms.Form):
    model = Artist
    fields = ['name', 'hometown', 'genre']
