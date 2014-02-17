__author__ = 'Kevin'
from django.views.generic import TemplateView
from bpmarchive.artists.models import Artist, Genre, Album, Track
from bpmarchive.artists.forms import ArtistForm, ArtistFormset, ArtistGenreFormset,  GenreFormset, GenreForm, TrackForm, TrackFormset, AlbumForm, AlbumFormset


class HomeView(TemplateView):
    template_name = "index.html";

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['ArtistForm'] = ArtistForm()
        context['GenreForm'] = GenreForm()
        return context
