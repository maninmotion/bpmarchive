__author__ = 'Kevin'
from .models import Artist, Genre
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory


#class ArtistForm(forms.form):
#class ArtistForm(forms.Form):
class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        form_class = Artist
    #fields = ['name', 'hometown', 'genre']
    fields = ['name', 'genre']


'''
class HometownForm(ModelForm):
    class Meta:
        model = Hometown
        form_class = Hometown
    fields = ['name', 'state', 'country']
'''


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        form_class = Genre
    fields = ['name', 'genretype']


ArtistFormset = formset_factory(ArtistForm)
GenreFormset = formset_factory(GenreForm)
ArtistGenreFormset = inlineformset_factory(Genre, Artist, extra=1)
#ArtistHometownFormset = inlineformset_factory(Hometown, Artist, extra=1)
