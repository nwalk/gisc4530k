"""
Outline:

class Classes

class Courses

class Instructors

class Locations

class Students

NOTE to developer: some field have been duplicated between models.

"""

from django.contrib.gis.db import models
from django.forms import ModelForm


# class Classes(models.Model):
#     """
#     Examples:
#     course: GISC 4360k Geo-spatial Web Development
#     status: complete, enrolled, incomplete
#     semester: spring 14, summer 14, fall 15
#     """
#     course = models.ForeignKey('Courses')
#     status = models.CharField(max_length=4)
#
#     def __str__(self):
#         return "{}-{}".format(self.course, self.status)


class Courses(models.Model):
    prefix = models.TextField(max_length=20)
    num = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    hr = models.CharField(max_length=20)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.prefix, self.num)


class Instructors(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    status = models.CharField(max_length=40)
    course = models.ForeignKey('Courses')

    def __str__(self):
        return "{}".format(self.last_name)


class Locations(models.Model):
    campus = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    room = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.campus)


class StudentClasses(models.Model):
    student = models.ForeignKey('Students')
    classes = models.ForeignKey('Courses')
    area = models.ForeignKey('Area')

    def __str__(self):
        return "{}".format(self.student)


class Area(models.Model):
    """
    ie. a, b, major curriculum, etc.
    """
    area = models.CharField(max_length=2)

    def __str__(self):
        return "{}".format(self.area)


class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_username = models.CharField(max_length=20, default='null')
    student_major = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    total_hours = models.IntegerField(max_length=3)

    def __str__(self):
        return "{}".format(self.first_name)