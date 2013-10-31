# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from django.core.urlresolvers import reverse

from models import Artist


def index(request):
    try:
        list_of_artists = Artist.objects.order_by('name')[:5]
    except Artist.DoesNotExist:
        raise Http404
    return render(request, 'artists/index.html', {'list_of_artists': list_of_artists})


def details(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artists/details.html', {'artist': artist})
