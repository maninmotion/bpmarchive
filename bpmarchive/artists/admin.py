__author__ = 'Kevin'
from django.contrib import admin
from .models import Artist, GenreType, Hometown, Genre


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['']}),
    ]

admin.site.register(Artist)
admin.site.register(GenreType)
admin.site.register(Genre)
admin.site.register(Hometown)
