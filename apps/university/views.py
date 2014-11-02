from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class ProfileView(generic.TemplateView):
    template_name = 'user/profile.html'


class PlanOfStudyView(generic.TemplateView):
    template_name = 'user/planofstudy.html'


class TranscriptsView(generic.TemplateView):
    template_name = 'user/transcripts.html'