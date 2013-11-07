__author__ = 'Kevin'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import ArtistsListView, DisplayArtistView, ArtistCreateView

urlpatterns = patterns('',
                       # ex /artist/5/
                       # FBVs routing
                       #url(r'^(?P<artist_id>\d+)/$', views.details, name='artist-detail'),
                       #url(r'^manage/(?P<artist_id>\d+)$', views.manage, name='artist-manage'),
                       #url(r'^(?P<artist_id>\d+)/manage/$', views.manage, name='artist-manage'),
                       #url(r'^$', views.index, name='index'),

                        url(r'^(?P<artist_id>\d+)/$', DisplayArtistView.as_view(), name='artist-detail'),
                        url(r'^create/$', ArtistCreateView.as_view(), name='artist-add'),
                        #url(r'^$', TemplateView.as_view(template_name='artists/index.html')),
                        url(r'^$', ArtistsListView.as_view()),

                       )

