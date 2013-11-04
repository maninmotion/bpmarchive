# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
#from django.core.urlresolvers import reverse

from models import Artist
from forms import ArtistForm


def index(request):
    #ArtistFormset = formset_factory(ArtistForm)
    ArtistFormset = ArtistForm(Artist)
    try:
        list_of_artists = Artist.objects.order_by('name')[:5]
    except Artist.DoesNotExist:
        raise Http404
    return render(request, 'artists/index.html', {'list_of_artists': list_of_artists, 'ArtistFormset': ArtistFormset})


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
