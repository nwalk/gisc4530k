import os
from django.contrib.gis.utils import LayerMapping
from models import Campuses
import django
django.setup()

campus_mapping = {
    'name' : 'Name',
    'lat' : 'Lat',
    'lon' : 'Long',
    'point' : 'POINT',
}
campus_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/ung_campus/campuses.shp'))


def run(verbose=True):
    lm = LayerMapping(Campuses, campus_shp, campus_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)




#
# univ_mapping = {
#     'name' : 'name',
#     'address' : 'address',
#     'city' : 'city',
#     'state' : 'state',
#     'telephone' : 'telephone',
#     'lat' : 'lat',
#     'lon' : 'lon',
#     'website' : 'website',
#     'point' : 'POINT',
# }
# univ_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/universities.shp'))
#
#
# def run(verbose=True):
#     lm = LayerMapping(Universities, univ_shp, univ_mapping,
#                       transform=False, encoding='iso-8859-1')
#
#     lm.save(strict=True, verbose=verbose)
