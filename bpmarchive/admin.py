__author__ = 'Kevin'
from django.contrib import admin
from artists.models import Artist


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['']}),
    ]

admin.site.register(ArtistAdmin)
