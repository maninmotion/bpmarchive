__author__ = 'Kevin'
from django.contrib import admin
from .models import Artist, GenreType, Genre, Track, Album


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['']}),
    ]

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(GenreType)
admin.site.register(Track)
