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

from models import Album, Track
from forms import AlbumForm, TrackForm, AlbumFormset, TrackFormset, AlbumTrackFormset
from serializers import AlbumSerializer, TrackSerializer


class AlbumListView(TemplateView):
    template_name = "tracks/index.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['list_of_albums'] = Album.objects.order_by('name')[:5]
        #context['artist_hometown_formset'] = ArtistHometownFormset()
        context['album_track_formset'] = AlbumTrackFormset()
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


class AlbumViewSet(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    #model = serializer_class.Meta.model
    search_fields = ('name', 'artist')

    def get_queryset(self, **kwargs):
        queryset = Album.objects.all().order_by('name').distinct()
        search_action = self.kwargs['action']
        search_term = self.request.QUERY_PARAMS['q']

        if search_term is not None and search_action == 'search':
            queryset = queryset.filter(name__icontains=search_term)
            #queryset = queryset.filter(name__icontains=search_term)
        return queryset


''' Track Views '''


class TrackListView(TemplateView):
    template_name = "tracks/index.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(TrackListView, self).get_context_data(**kwargs)
        context['list_of_tracks'] = Track.objects.order_by('name')[:5]
        #context['artist_hometown_formset'] = ArtistHometownFormset()
        context['album_track_formset'] = AlbumTrackFormset()
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
    fields = ['name', 'artist','bpm']

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



class TrackViewSet(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    #model = serializer_class.Meta.model
    search_fields = ('name', 'artist','bpm')

    def get_queryset(self, **kwargs):
        queryset = Track.objects.all().order_by('name').distinct()
        search_action = self.kwargs['action']
        search_term = self.request.QUERY_PARAMS['q']

        if search_term is not None and search_action == 'search':
            queryset = queryset.filter(name__icontains=search_term)
            #queryset = queryset.filter(name__icontains=search_term)
        return queryset

