from django.conf.urls import patterns, include, url
from django.contrib import admin


api_patterns = patterns('',
    url(r'^', include('apps.university.api_urls'), name='classes'),
    url(r'^', include('apps.university.api_urls'), name='courses'),
    url(r'^', include('apps.university.api_urls'), name='instructors'),
    url(r'^', include('apps.university.api_urls'), name='locations'),
)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.university.urls', namespace='home')),
    url(r'api/v1/', include(api_patterns, namespace='api')),
)
