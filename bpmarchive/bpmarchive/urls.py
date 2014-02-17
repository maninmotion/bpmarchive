from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import HomeView
from artists.views import IndexView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', HomeView.as_view(template_name='index.html')),
    url(r'^$', IndexView.as_view(), name='index-view'),
    #url(r'^$', TemplateView.as_view(template_name='base.html')),


    # Examples:
    #url(r'^$', 'bpmarchive.views.home', name='home'),
    # url(r'^bpmarchive/', include('bpmarchive.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artists/', include('artists.urls')),
    url(r'^tracks/', include('tracks.urls')),
)
