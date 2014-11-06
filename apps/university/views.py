from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse
from django.template.loader import render_to_string

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


class CoursesCreate(generic.edit.CreateView):
    """This form adds data to the database"""
    model = models.Courses
    success_url = '/profile'


class CoursesUpdate(generic.edit.UpdateView):
    """This is like the create view, different button"""
    model = models.Courses
    success_url = '/profile'


class CoursesDelete(generic.edit.DeleteView):
    model = models.Courses
    success_url = '/profile'

# """ items list """
#
#
# class ProfileView(generic.ListView):
#     model = models.Courses
#     template_name = 'user/profile.html'
#
#     def get_queryset(self):
#         return models.Courses.objects.all()
#
# """ Edit item """
#
#
# class CoursesCreate(generic.edit.CreateView):
#     model = models.Courses
#     # form_class = ItemForm
#     template_name = 'courses_form.html'
#
#     def dispatch(self, *args, **kwargs):
#         self.item_id = kwargs['pk']
#         return super(CoursesCreate, self).dispatch(*args, **kwargs)
#
#     def form_valid(self, form):
#         form.save()
#         item = models.Courses.objects.get(id=self.item_id)
#         return HttpResponse(render_to_string('university/item_create_success.html', {'item': item}))