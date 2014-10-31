from django.conf.urls import patterns, include, url
from apps.university import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(views.HomeView.as_view())),
    url(r'^map$', views.MapView.as_view(), name='map'),
    )
