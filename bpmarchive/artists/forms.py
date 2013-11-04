__author__ = 'Kevin'
from .models import Artist
from django.forms import ModelForm


class ArtistForm(ModelForm):
    model = Artist
    fields = ['name', 'hometown', 'genre']
