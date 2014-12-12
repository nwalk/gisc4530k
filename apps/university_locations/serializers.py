from apps.university_locations import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

# REST framework serializer
# http://www.django-rest-framework.org/tutorial/quickstart


class UniversitiesSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Universities
        geo_field = 'point'
        fields = ('name', 'address', 'city', 'state', 'telephone', 'website', 'lat', 'lon')


class CampusSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Campuses
        geo_field = 'point'
        fields = ('name', 'lat', 'lon')