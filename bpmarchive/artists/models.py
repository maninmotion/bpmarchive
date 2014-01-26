from django.db import models
from django.forms import ModelForm, DateTimeField

__author__ = 'Kevin'
from django.db import models


'''
class Hometown(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
'''


class GenreType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    genretype = models.ForeignKey(GenreType)

    def __unicode__(self):
        return '%s > %s' % (self.genretype.name, self.name)
        #return GenreType + " | " + self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)
    #hometown = models.ForeignKey(Hometown)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=1999)
    artist = models.ForeignKey('Artist')

    def __unicode__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    bpm = models.IntegerField()
    album = models.ForeignKey('Album')

    def __unicode__(self):
        return self.name


