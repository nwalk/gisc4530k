from django.views import generic
from . import models

class HomeView(generic.TemplateView):
    template_name = 'home.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class ProfileView(generic.edit.CreateView):
    template_name = 'user/profile.html'
    model = models.Courses
    success_url = '/profile'


class PlanOfStudyView(generic.TemplateView):
    template_name = 'user/planofstudy.html'


class TranscriptsView(generic.TemplateView):
    template_name = 'user/transcripts.html'


# class CoursesCreate(generic.edit.CreateView):
#     """This form adds data to the database"""
#     model = models.Courses
#     success_url = '/profile'



class CoursesUpdate(generic.edit.UpdateView):
    """This is like the create view, different button"""
    model = models.Courses
    success_url = '/profile'


class CoursesDelete(generic.edit.DeleteView):
    model = models.Courses
    success_url = '/profile'


