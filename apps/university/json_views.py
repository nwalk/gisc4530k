from apps.university import models, serializers
from rest_framework import generics
import django_filters

# views section of quick start guide
# http://www.django-rest-framework.org/tutorial/quickstart


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class ClassesFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Classes
        fields = ['id']


class ClassesCollection(generics.ListAPIView):
    queryset = models.Classes.objects.all()
    serializer_class = serializers.ClassesSerializer
    filter_class = ClassesFilter


class CoursesFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Courses
        fields = ['id', 'prefix', 'number', 'title', 'hours']


class CoursesCollection(generics.ListAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = serializers.CoursesSerializer
    filter_class = CoursesFilter


class InstructorsFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Instructors
        fields = ['id']


class InstructorsCollection(generics.ListAPIView):
    queryset = models.Instructors.objects.all()
    serializer_class = serializers.InstructorsSerializer
    filter_class = InstructorsFilter


class LocationsFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Locations
        fields = ['id', 'campus', 'building', 'room']


class LocationsCollection(generics.ListAPIView):
    queryset = models.Locations.objects.all()
    serializer_class = serializers.LocationsSerializer
    filter_class = LocationsFilter