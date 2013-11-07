__author__ = 'Kevin'
from .models import Artist, Genre, Hometown
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory


#class ArtistForm(forms.form):
#class ArtistForm(forms.Form):
class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        form_class = Artist
    fields = ['name', 'hometown', 'genre']


ArtistFormset = formset_factory(ArtistForm)
ArtistGenreFormset = inlineformset_factory(Genre, Artist, extra=1)
ArtistHometownFormset = inlineformset_factory(Hometown, Artist, extra=1)
