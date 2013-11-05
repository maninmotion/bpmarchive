# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.views.generic import TemplateView, RedirectView
#from django.core.urlresolvers import reverse

from models import Artist
from forms import ArtistFormset, ArtistGenreFormset, ArtistHometownFormset


class ArtistsListView(TemplateView):
    template_name = "artists/index.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(ArtistsListView, self).get_context_data(**kwargs)
        context['list_of_artists'] = Artist.objects.order_by('name')[:5]
        context['artist_hometown_formset'] = ArtistHometownFormset()
        context['artist_genre_formset'] = ArtistGenreFormset()
        context['artist_formset'] = ArtistFormset()
        return context


class DisplayArtistView(TemplateView):
    template_name = "artists/details.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayArtistView, self).get_context_data(**kwargs)
        context['artist'] = Artist.objects.get(pk=self.kwargs.get('artist_id', None))
        return context


'''
# old CBVs
def index(request):
    ArtistFormset = formset_factory(ArtistForm)
    #ArtistFormset = ArtistForm(Artist)
    try:
        list_of_artists = Artist.objects.order_by('name')[:5]
    except Artist.DoesNotExist:
        raise Http404

    artist_formset = ArtistFormset(prefix='artists')
    return render(request, 'artists/index.html', {'list_of_artists': list_of_artists, 'artist_formset': artist_formset})


def details(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artists/details.html', {'artist': artist})


def add_artist(request):
    artistFormSet = modelformset_factory(Artist)
    if request.method == 'POST':
        formset = artistFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = artistFormSet()
    return render_to_response("artists/index.html", {
        "formset": formset,
    })
'''
