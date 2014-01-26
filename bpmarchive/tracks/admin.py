__author__ = 'Kevin'
from django.contrib import admin
from .models import Track, Album


class TrackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['']}),
    ]

admin.site.register(Track)
admin.site.register(Album)
