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


class Classes(models.Model):
    """
    Examples:
    course: GISC 4360k Geo-spatial Web Development
    status: complete, enrolled, incomplete
    semester: spring 14, summer 14, fall 15
    """
    course = models.ForeignKey('Courses')
    status = models.CharField(max_length=4)

    def __str__(self):
        return "{}-{}".format(self.course, self.status)


class Courses(models.Model):
    """
    Examples:
    prefix: GISC
    number: 4360k
    title: Geo-spatial Web Development
    """
    prefix = models.TextField(max_length=10)
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    hours = models.IntegerField(max_length=2)
    location = models.ForeignKey('Locations')

    def __str__(self):
        return "{}-{}".format(self.prefix, self.number)


class Instructors(models.Model):
    """
    first_name: James
    last_name: Jones
    status: Adjunct
    university: University of North Georgia
    course: one to many relationship
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    status = models.CharField(max_length=40)
    course = models.ForeignKey('Courses')

    def __str__(self):
        return "{}".format(self.last_name)


class Locations(models.Model):
    """
    campus: Some City
    building: Some Building
    room: 967
    """
    campus = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    room = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.campus)


class Students(models.Model):
    """
    first_name: jon
    last_name: doe
    student_id: 7777777
    student_major: UnderWater Basket Weaving
    status: Full Time
    total_hours: 36
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.IntegerField(max_length=10)
    student_major = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    total_hours = models.IntegerField(max_length=3)

    def __str__(self):
        return "{}".format(self.first_name)