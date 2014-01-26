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
from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import filters
from rest_framework.views import APIView
import django_filters

from models import Artist, Genre, Album, Track
from forms import ArtistForm, ArtistFormset, ArtistGenreFormset,  GenreFormset, GenreForm, TrackForm, TrackFormset, AlbumForm, AlbumFormset

from serializers import GenreSerializer, TrackSerializer, AlbumSerializer, ArtistSerializer


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


class AlbumListView(TemplateView):
    template_name = "tracks/index.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['list_of_albums'] = Album.objects.order_by('name')[:5]
        #context['artist_hometown_formset'] = ArtistHometownFormset()
        #context['album_track_formset'] = AlbumTrackFormset()
        context['album_formset'] = AlbumFormset()
        context['AlbumForm'] = AlbumForm()
        context['TrackForm'] = TrackForm()
        return context


class DisplayAlbumView(TemplateView):
    template_name = "tracks/details.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayAlbumView, self).get_context_data(**kwargs)
        context['album'] = Album.objects.get(pk=self.kwargs.get('artist_id', None))
        return context


class AlbumCreateView(generic.CreateView):
    template_name = "tracks/index.html"
    model = Album
    form_class = AlbumForm
    fields = ['name', 'artist']
    success_url = "tracks/index.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #process data
            self.object = form.save()
            return HttpResponseRedirect('/tracks/')
        else:
            return HttpResponseRedirect('/tracks/')


'''
class AlbumCreateView(generic.CreateView):
#class ArtistCreateView(FormView):
    template_name = "tracks/albumCreate.html"
    model = Album
    form_class = AlbumForm
    fields = ['name', 'artist']

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


# https://pypi.python.org/pypi/django-datatables-view
class AlbumViewSet(BaseDatatableView):
    model = Album
    columns = ['name', 'artist']
    order_columns = ['name', 'artist']
    max_display_length = 100

    def render_column(self, row, column):
        if column == 'artist':
            return '%s' % row.artist
        else:
            return super(AlbumViewSet, self).render_column(row, column)

    def filter_queryset(self, qs):
        if self.request.method == 'POST':
            sSearch = self.request.POST.get('sSearch', None)
        elif self.request.method == 'GET':
            sSearch = self.request.GET.get('sSearch', None)

        if sSearch:
            qs = qs.filter(name__icontains=sSearch)
        return qs


'''
class AlbumViewSet(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    #model = serializer_class.Meta.model
    search_fields = ('name', 'artist')

    def get_queryset(self, **kwargs):
        queryset = Album.objects.all().order_by('name').distinct()
        search_action = self.kwargs['action']
        search_term = self.request.QUERY_PARAMS.get('q', None)
        #search_term = self.request.QUERY_PARAMS['q']

        if search_term is not None and search_action == 'search':
            queryset = queryset.filter(name__icontains=search_term)
            #queryset = queryset.filter(name__icontains=search_term)
        elif search_action == 'all':
            queryset = queryset

        return queryset
'''



''' Track Views '''


class TrackListView(TemplateView):
    template_name = "artists/tracks.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(TrackListView, self).get_context_data(**kwargs)
        context['list_of_tracks'] = Track.objects.order_by('name')[:5]
        #context['artist_hometown_formset'] = ArtistHometownFormset()
        #context['album_track_formset'] = AlbumTrackFormset()
        context['track_formset'] = TrackFormset()
        context['AlbumForm'] = AlbumForm()
        context['TrackForm'] = TrackForm()
        return context


class DisplayTrackView(TemplateView):
    template_name = "tracks/details.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayTrackView, self).get_context_data(**kwargs)
        context['track'] = Track.objects.get(pk=self.kwargs.get('artist_id', None))
        return context


'''
class TrackCreateView(generic.CreateView):
    template_name = "tracks/index.html"
    model = Track
    form_class = TrackForm
    fields = ['name', 'album', 'bpm']
    success_url = "tracks/index.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #process data
            self.object = form.save()
            return HttpResponseRedirect('/tracks/')
        else:
            return HttpResponseRedirect('/tracks/')
'''


class TrackCreateView(generic.CreateView):
#class ArtistCreateView(FormView):
    template_name = "tracks/trackCreate.html"
    model = Track
    form_class = TrackForm
    fields = ['name', 'artist', 'bpm']

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


class TrackViewSet(BaseDatatableView):
    model = Track
    columns = ['name', 'album.name', 'bpm']
    order_columns = ['name', 'album', 'bpm']
    max_display_length = 100

    def render_column(self, row, column):
        if column == 'artist':
            return '%s' % row.artist
        else:
            return super(TrackViewSet, self).render_column(row, column)

    def filter_queryset(self, qs):
        if self.request.method == 'POST':
            sSearch = self.request.POST.get('sSearch', None)
        elif self.request.method == 'GET':
            sSearch = self.request.GET.get('sSearch', None)

        if sSearch:
            qs = qs.filter(name__icontains=sSearch)
            #qs = qs.filter(name__istartswith=sSearch)
        return (qs)




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
