__author__ = 'Kevin'
from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # ex /artist/5/
                       url(r'^(?P<artist_id>\d+)/$', views.details, name='artist-detail'),
                       #url(r'^manage/(?P<artist_id>\d+)$', views.manage, name='artist-manage'),
                       #url(r'^(?P<artist_id>\d+)/manage/$', views.manage, name='artist-manage'),

                       )

