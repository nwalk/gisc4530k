from django.contrib.gis.db import models


class Students(models.Model):
    """Model for student information"""
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    student_id = models.IntegerField(max_length=9)
    student_major = models.CharField(max_length=50)
    status = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Instructors(models.Model):
    """Model for instructor information"""
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Courses(models.Model):
    """Model for course information"""
    CRN = models.IntegerField(max_length=4)
    section = models.IntegerField(max_length=2)
    course = models.CharField(max_length=10)
    session = models.TextField(max_length=15)
    title = models.CharField(max_length=40)
    hours = models.IntegerField(max_length=1)
    location = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Classes(models.Model):
    """An instant of courses"""
    course = models.CharField(max_length=40)
    date_taken = models.DateField()

    def __str__(self):
        return "{}".format(self.name)


class Locations(models.Model):
    """Model for location information"""
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)