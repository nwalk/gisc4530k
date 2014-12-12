from apps.university_locations import models, serializers
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


class UniversityFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Universities
        fields = ['name', 'address', 'city', 'state', 'telephone', 'website', 'lat', 'lon']


class UniversityCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Universities.objects.all()
    serializer_class = serializers.UniversitiesSerializer
    filter_class = UniversityFilter


class CampusFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Campuses
        fields = ['name', 'lat', 'lon']


class CampusCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Campuses.objects.all()
    serializer_class = serializers.CampusSerializer
    filter_class = CampusFilter