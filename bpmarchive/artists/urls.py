__author__ = 'Kevin'
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArtistsListView, DisplayArtistView, ArtistCreateView, GenreViewSet, GenreCreateView

#router = routers.DefaultRouter();
router = routers.SimpleRouter()
#router.register(r'^genres/(?P<q>.+)/$', GenreViewSet.as_view(), base_name='genre_list')
#router.register(r'^genres/(?P<q>\d+)$', GenreViewSet.as_view(), base_name='genre_list')
#router.register(r'^genres/(?P<q>.+)', GenreViewSet.as_view(), base_name='genre_list')
#router.register(r'^genres/(?P<term>\w+)/$', GenreViewSet, base_name='genre_list'),

urlpatterns = patterns('',
                       # ex /artist/5/
                       # FBVs routing
                       #url(r'^(?P<artist_id>\d+)/$', views.details, name='artist-detail'),
                       #url(r'^manage/(?P<artist_id>\d+)$', views.manage, name='artist-manage'),
                       #url(r'^(?P<artist_id>\d+)/manage/$', views.manage, name='artist-manage'),
                       #url(r'^$', views.index, name='index'),

                       url(r'^', include(router.urls)),
                       url(r'^(?P<artist_id>\d+)/$', DisplayArtistView.as_view(), name='artist-detail'),
                       url(r'^create/$', ArtistCreateView.as_view(), name='artist-add'),
                       url(r'^genreCreate/$', GenreCreateView.as_view(), name='genre-add'),
                       url(r'^$', ArtistsListView.as_view(), name='artist-home'),

                       url(r'^genres/(?P<action>\w+)/$', GenreViewSet.as_view(), name='genre_list'),

                       #url(r'^genres/(?P<q>\d+)$', GenreViewSet.as_view(), name='genre_list')

                       #url(r'^$', TemplateView.as_view(template_name='artists/index.html')),

                       )

