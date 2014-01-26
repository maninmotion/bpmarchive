__author__ = 'Kevin'
from .models import Artist, Genre, Track, Album
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



class AlbumForm(ModelForm):
    class Meta:
        model = Album
        form_class = Album
        #fields = ['name', 'hometown', 'genre']
    fields = ['name', 'year', 'artist']


class TrackForm(ModelForm):
    class Meta:
        model = Track
        form_class = Track
    fields = ['name', 'bpm', 'album']


ArtistFormset = formset_factory(ArtistForm)
GenreFormset = formset_factory(GenreForm)
ArtistGenreFormset = inlineformset_factory(Genre, Artist, extra=1)
#ArtistHometownFormset = inlineformset_factory(Hometown, Artist, extra=1)
AlbumFormset = formset_factory(AlbumForm)
TrackFormset = formset_factory(TrackForm)
AlbumTrackFormset = inlineformset_factory(Album, Track, extra=1)
