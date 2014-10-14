from django.conf.urls import patterns, include, url
from apps.university import views
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view()),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^mapview$', views.MapView.as_view(), name='mapview'),
    )