# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.views.generic import TemplateView, FormView
from django.views import generic
#from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from rest_framework import viewsets, generics, views
from rest_framework import filters
from rest_framework.views import APIView
import django_filters

from models import Artist, Genre
from forms import ArtistForm, ArtistFormset, ArtistGenreFormset,  GenreFormset, GenreForm
from serializers import GenreSerializer


class ArtistsListView(TemplateView):
    template_name = "artists/index.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(ArtistsListView, self).get_context_data(**kwargs)
        context['list_of_artists'] = Artist.objects.order_by('name')[:5]
        #context['artist_hometown_formset'] = ArtistHometownFormset()
        context['artist_genre_formset'] = ArtistGenreFormset()
        context['artist_formset'] = ArtistFormset()
        context['ArtistForm'] = ArtistForm()
        context['GenreForm'] = GenreForm()
        return context


class DisplayArtistView(TemplateView):
    template_name = "artists/details.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayArtistView, self).get_context_data(**kwargs)
        context['artist'] = Artist.objects.get(pk=self.kwargs.get('artist_id', None))
        return context


class ArtistCreateView(generic.CreateView):
#class ArtistCreateView(FormView):
    template_name = "artists/index.html"
    model = Artist
    form_class = ArtistForm
    #fields = ['name', 'hometown', 'genre']
    fields = ['name', 'genre']
    success_url = "artists/index.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #artist_form = form['artist_formset']
        if form.is_valid():
            #process data
            self.object = form.save()
            #artist_form.instance = self.object
            #artist_form.save()
            return HttpResponseRedirect('/artists/')
        else:
            return HttpResponseRedirect('/artists/')


class GenreCreateView(generic.CreateView):
#class ArtistCreateView(FormView):
    template_name = "artists/genreCreate.html"
    model = Genre
    form_class = GenreForm
    fields = ['name', 'genretype']

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #artist_form = form['artist_formset']
        if form.is_valid():
            #process data
            message = 'Success'
            self.object = form.save()
            return HttpResponse(message)
        else:
            message = 'Error'
            return HttpResponse(message)


'''
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('genretype', 'name')
    serializer_class = GenreSerializer
'''


#class GenreViewSet(APIView):
#class GenreViewSet(viewsets.ModelViewSet):
class GenreViewSet(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    #model = serializer_class.Meta.model
    search_fields = ('name', 'genretype')
    #filter_backends = (filters.DjangoFilterBackend,)
    #queryset = Genre.objects.all()

    def get_queryset(self, **kwargs):
        queryset = Genre.objects.all().order_by('genretype', 'name').distinct()
        search_action = self.kwargs['action']
        search_term = self.request.QUERY_PARAMS['q']

        if search_term is not None and search_action == 'search':
            queryset = queryset.filter(Q(genretype__name__icontains=search_term) | Q(name__icontains=search_term))
            #queryset = queryset.filter(name__icontains=search_term)
        return queryset




'''
    def get(self, request, format='JSON'):
        queryset = Genre.objects.all().order_by('genretype', 'name')
        #searchterm = request.QUERY_PARAMS.get('term', None)
        searchterm = request['term']
        if searchterm is not None:
            queryset = queryset.filter(name=searchterm)
        return queryset
'''





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
