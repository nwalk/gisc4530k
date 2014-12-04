from django.views import generic
from . import models
from django.db.models import Sum


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class PlanOfStudyView(generic.edit.CreateView):
    template_name = 'user/planofstudy.html'
    model = models.StudentClasses
    # hours = models.Courses.objects.aggregate(Sum('hr'))
    # hours = models.StudentClasses.objects.aggregate(Sum(''))
    success_url = '/planofstudy'

    def get_context_data(self, **kwargs):
        context = super(PlanOfStudyView, self).get_context_data(**kwargs)
        context['AREA_A'] = models.StudentClasses.objects.filter(student__user__pk=self.request.user.pk,
                                                                 area__name='A')
        context['AREA_B'] = models.StudentClasses.objects.filter(student__user__pk=self.request.user.pk,
                                                                 area__name='B')
        context['AREA_C'] = models.StudentClasses.objects.filter(student__user__pk=self.request.user.pk,
                                                                 area__name='C')
        context['AREA_D'] = models.StudentClasses.objects.filter(student__user__pk=self.request.user.pk,
                                                                 area__name='D')
        context['AREA_E'] = models.StudentClasses.objects.filter(student__user__pk=self.request.user.pk,
                                                                 area__name='E')
        context['AREA_F'] = models.StudentClasses.objects.filter(student__user__pk=self.request.user.pk,
                                                                 area__name='F')
        return context


class ProfileView(generic.edit.UpdateView):
    template_name = 'user/profile.html'
    model = models.Students
    success_url = '/profile'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['s_profile'] = models.Students.objects.filter(user__pk=self.request.user.pk).first()
        return context


class TranscriptsView(generic.TemplateView):
    template_name = 'user/transcripts.html'


# class CoursesCreate(generic.edit.CreateView):
#     """This form adds data to the database"""
#     model = models.Courses
#     success_url = '/profile'


class StudentClasses(generic.ListView):
    model = models.Courses
    template_name = 'user/profile.html'
    # queryset = models.Courses.objects.aggregate(Sum('hr'))
    queryset = models.Courses.objects.filter()


class CoursesUpdate(generic.edit.UpdateView):
    """This is like the create view, different button"""
    model = models.Courses
    success_url = '/profile'


class CoursesDelete(generic.edit.DeleteView):
    model = models.Courses
    success_url = '/profile'


