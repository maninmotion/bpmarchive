__author__ = 'Kevin'
from .models import Genre, GenreType, Artist, Track, Album
from rest_framework import serializers


#class GenreSerializer(serializers.HyperlinkedModelSerializer):
class GenreSerializer(serializers.ModelSerializer):
    genretype = serializers.RelatedField()
    #genrelabel = genretype
    #genrelabel = '%s > %s' % (genretype, 'name')

    class Meta:
        model = Genre
        #fields = ('name', 'genrelabel')
        fields = ('id', 'name', 'genretype')


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre')


class AlbumSerializer(serializers.ModelSerializer):
    #genretype = serializers.RelatedField()

    class Meta:
        model = Album
        fields = ('id', 'name', 'artist')


class TrackSerializer(serializers.ModelSerializer):
    #genretype = serializers.RelatedField()

    class Meta:
        model = Track
        fields = ('id', 'album', 'bpm')
