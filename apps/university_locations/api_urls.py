from django.conf.urls import patterns, include, url
from apps.university_locations import json_views

urlpatterns = patterns('',
    url('^universities$', json_views.UniversityCollection.as_view(), name='universities'),
    url('^campus$', json_views.CampusCollection.as_view(), name='campus'),
    )