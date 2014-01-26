__author__ = 'Kevin'
from django.db import models
import bpmarchive


class Album(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=1999)
    artist = models.ForeignKey('artists.Artist')

    def __unicode__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    bpm = models.IntegerField()
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.name


