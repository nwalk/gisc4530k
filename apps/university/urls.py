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
    # url(r'^profile$', views.CoursesCreate.as_view(), name="course_create"),
    url(r'^update/(?P<pk>\d+)/$', views.CoursesUpdate.as_view(), name="course_update"),
    url(r'^delete/(?P<pk>\d+)/$', views.CoursesDelete.as_view(), name="course_delete"),
    )
