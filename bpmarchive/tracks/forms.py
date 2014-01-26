__author__ = 'Kevin'
from .models import Album, Track
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory


#class ArtistForm(forms.form):
#class ArtistForm(forms.Form):
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
    fields = ['name', 'bpm', 'artist']


AlbumFormset = formset_factory(AlbumForm)
TrackFormset = formset_factory(TrackForm)
AlbumTrackFormset = inlineformset_factory(Album, Track, extra=1)
#ArtistHometownFormset = inlineformset_factory(Hometown, Artist, extra=1)
