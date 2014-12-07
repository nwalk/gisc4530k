from django.conf.urls import patterns, include, url
from django.contrib import admin


api_patterns = patterns('',
    url(r'^', include('apps.university.api_urls')),
    url(r'^', include('apps.university_locations.api_urls')),
    # url(r'^', include('apps.university.api_urls')),
    # url(r'^', include('apps.university.api_urls')),
)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', include('apps.university.urls', namespace='home')),
    url(r'api/v1/', include(api_patterns, namespace='api')),
)
