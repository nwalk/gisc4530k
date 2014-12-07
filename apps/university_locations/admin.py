from django.contrib import admin
from django.contrib.gis import admin
from models import Universities

admin.site.register(Universities, admin.GeoModelAdmin)