from django.conf.urls import patterns, include, url
from apps.university import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view()),
    url(r'^map$', views.MapView.as_view(), name='map'),
    url(r'^profile$', login_required(views.ProfileView.as_view())),
    url(r'^planofstudy$', login_required(views.PlanOfStudyView.as_view())),
    url(r'^transcripts$', login_required(views.TranscriptsView.as_view())),
    )
