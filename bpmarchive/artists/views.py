# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.views.generic import TemplateView, FormView
from django.views import generic
#from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin

from models import Artist
from forms import ArtistForm, ArtistFormset, ArtistGenreFormset, ArtistHometownFormset


class ArtistsListView(TemplateView):
    template_name = "artists/index.html"

    def get_context_data(self, **kwargs):
        #ArtistFormset = formset_factory(ArtistForm)
        context = super(ArtistsListView, self).get_context_data(**kwargs)
        context['list_of_artists'] = Artist.objects.order_by('name')[:5]
        context['artist_hometown_formset'] = ArtistHometownFormset()
        context['artist_genre_formset'] = ArtistGenreFormset()
        context['artist_formset'] = ArtistFormset()
        context['ArtistForm'] = ArtistForm()
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
    fields = ['name', 'hometown', 'genre']
    success_url = "artists/index.html"

#    def form_valid(self, form):
#        context = self.get_context_data()
#        artist_form = context['artist_formset']
#        if artist_form.is_valid():
#            self.object = form.save()
#            artist_form.instance = self.object
#            artist_form.save()
#            return HttpResponseRedirect('/artist/index.html')

#        return HttpResponseRedirect('/artist/index.html')

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
