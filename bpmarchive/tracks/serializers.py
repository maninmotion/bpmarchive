__author__ = 'Kevin'
from .models import Album, Track
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    #genretype = serializers.RelatedField()

    class Meta:
        model = Album
        fields = ('id', 'name', 'artist')


class TrackSerializer(serializers.ModelSerializer):
    #genretype = serializers.RelatedField()

    class Meta:
        model = Track
        fields = ('id', 'artist', 'bpm')
