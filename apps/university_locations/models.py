from django.db import models


class Universities(models.Model):
    """Regular Django fields corresponding to the attributes in the
    universities shapefile."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.TextField(max_length=30)
    state = models.CharField('State', max_length=2)
    telephone = models.CharField('Phone Number', max_length=12)
    website = models.CharField('Website')

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name
