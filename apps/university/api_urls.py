from django.conf.urls import patterns, include, url
from apps.university import json_views

urlpatterns = patterns('',
    # url('^classes$', json_views.ClassesCollection.as_view(), name='classes'),
    url('^studentclasses$', json_views.StudentClassesCollection.as_view(), name='studentclasses'),
    url('^courses$', json_views.CoursesCollection.as_view(), name='courses'),
    url('^instructors$', json_views.InstructorsCollection.as_view(), name='instructors'),
    url('^locations$', json_views.LocationsCollection.as_view(), name='locations'),
)
