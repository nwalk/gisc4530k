from django.conf.urls import patterns, include, url
from apps.university import views
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', views.HomeView.as_view()),

)