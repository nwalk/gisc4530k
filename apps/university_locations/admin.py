from django.contrib import admin
from django.contrib.gis import admin
from models import Universities, Campuses

admin.site.register(Universities, admin.GeoModelAdmin)
admin.site.register(Campuses, admin.GeoModelAdmin)