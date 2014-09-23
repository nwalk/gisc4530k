from django.contrib.gis.db import models

class University(models.Model):
    """This is a model of no consequence"""
    name = models.CharField(max_length=40)
    status = models.BooleanField()
    desc = models.CharField(max_length=280)

    def __str__(self):
        return "{}".format(self.name)
