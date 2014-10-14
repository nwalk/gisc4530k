from apps.university import models
from rest_framework import serializers

# REST framework serializer
# http://www.django-rest-framework.org/tutorial/quickstart


class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Classes
        # json id field is called pk in Django-rest-framework
        fields = ('id', 'course', 'title', 'university')


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Courses
        fields = ('id', 'crn', 'section', 'course', 'title')


class InstructorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Instructors
        fields = ('id', 'first_name', 'last_name', 'university')


class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Locations
        fields = ('id', 'campus', 'building', 'room')