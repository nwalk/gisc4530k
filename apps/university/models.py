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
    time_period: SP15
    university: University of North Georgia
    completion_date: 10/10/10
    """
    course = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    time_period = models.CharField(max_length=4)
    university = models.CharField(max_length=40)
    completion_date = models.DateField()

    def __str__(self):
        return "{}".format(self.name)


class Courses(models.Model):
    """
    Examples:
    CRN: 4256
    section: 02
    course: GISC 4360k
    session: summer full
    title: Geo-spatial Web Development
    hours: 3
    location: Technology complex rm 659
    instructor: Dr James Jones
    """
    CRN = models.IntegerField(max_length=4)
    section = models.IntegerField(max_length=2)
    course = models.CharField(max_length=10)
    session = models.TextField(max_length=15)
    title = models.CharField(max_length=40)
    hours = models.IntegerField(max_length=1)
    location = models.CharField(max_length=50)
    instructor = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Instructors(models.Model):
    """
    first_name: James
    last_name: Jones
    status: Adjunct
    university: University of North Georgia
    course: one to many relationship
    """
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    status = models.CharField(max_length=40)
    university = models.CharField(max_length=20)
    course = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Locations(models.Model):
    """
    campus: Some City
    building: Some Building
    room: 967
    """
    campus = models.CharField(max_length=40)
    building = models.CharField(max_length=40)
    room = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Students(models.Model):
    """
    first_name: jon
    last_name: doe
    student_id: 7777777
    student_major: UnderWater Basket Weaving
    status: Full Time
    total_hours: 36
    """
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    student_id = models.IntegerField(max_length=9)
    student_major = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    total_hours = models.IntegerField(max_length=3)

    def __str__(self):
        return "{}".format(self.name)