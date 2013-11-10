__author__ = 'Kevin'
from .models import Genre, GenreType, Hometown
from rest_framework import serializers


#class GenreSerializer(serializers.HyperlinkedModelSerializer):
class GenreSerializer(serializers.ModelSerializer):
    genretype = serializers.RelatedField()
    #genrelabel = genretype
    #genrelabel = '%s > %s' % (genretype, 'name')

    class Meta:
        model = Genre
        #fields = ('name', 'genrelabel')
        fields = ('name', 'genretype')
