# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from models import Artist


def index(request):
    list_of_artists = Artist.objects
    template = loader.get_template('artists/index.html')
    context = RequestContext(request, {
        'list_of_artists': list_of_artists
    })
    return render(request, 'artists/index.html', context)
