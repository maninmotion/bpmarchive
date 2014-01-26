__author__ = 'Kevin'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AlbumCreateView, AlbumListView, DisplayAlbumView, AlbumViewSet, TrackCreateView, TrackListView, \
    DisplayTrackView, TrackViewSet

router = routers.SimpleRouter()
#router.register(r'^genres/(?P<q>.+)/$', GenreViewSet.as_view(), base_name='genre_list')
#router.register(r'^genres/(?P<q>\d+)$', GenreViewSet.as_view(), base_name='genre_list')
#router.register(r'^genres/(?P<q>.+)', GenreViewSet.as_view(), base_name='genre_list')
#router.register(r'^genres/(?P<term>\w+)/$', GenreViewSet, base_name='genre_list'),

urlpatterns = patterns('',

                       url(r'^', include(router.urls)),
                       url(r'^(?P<album_id>\d+)/$', DisplayAlbumView.as_view(), name='album-detail'),
                       url(r'^create/$', AlbumCreateView.as_view(), name='album-add'),
                       url(r'^albumCreate/$', AlbumCreateView.as_view(), name='album-add'),
                       #url(r'^$', AlbumListView.as_view(), name='album-home'),

                       url(r'^albums/(?P<action>\w+)/$', AlbumViewSet.as_view(), name='album_list'),


                       url(r'^(?P<track_id>\d+)/$', DisplayTrackView.as_view(), name='track-detail'),
                       url(r'^createtrack/$', TrackCreateView.as_view(), name='track-add'),
                       url(r'^trackCreate/$', TrackCreateView.as_view(), name='track-add'),
                       url(r'^$', TrackListView.as_view(), name='track-home'),

                       url(r'^tracks/(?P<action>\w+)/$', TrackViewSet.as_view(), name='track_list'),


                       #url(r'^genres/(?P<q>\d+)$', GenreViewSet.as_view(), name='genre_list')

                       #url(r'^$', TemplateView.as_view(template_name='artists/index.html')),

                       )

