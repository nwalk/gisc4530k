from django.contrib import admin
from apps.university import models

admin.site.register(models.Students)
admin.site.register(models.Instructors)
admin.site.register(models.Courses)
admin.site.register(models.StudentClasses)
admin.site.register(models.Locations)
admin.site.register(models.Area)
# admin.site.register(models.PlanOfStudy)