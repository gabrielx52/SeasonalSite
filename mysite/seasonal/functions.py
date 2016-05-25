import zipcode
from .models import Produce, Location


def local_zipcodes_models(startingzip='98119', radius=10):
    """ Returns list of Location models within radius of startingzip """
    zip_obj = zipcode.isequal(startingzip)
    location_objects = set()
    try:
        local_zips = zipcode.isinradius((zip_obj.lat, zip_obj.lon), radius)
        zip_list = [i.zip for i in local_zips]
        for zip_code in zip_list:
            location_object = Location.objects.filter(zipcode=zip_code)
            location_objects.update(location_object)
        return location_objects
    except AttributeError:
        return 'No surrounding data available for ' + startingzip


def multi_zipcode_growzone_compiler(zipcode_model_list):
    """ Compiles all grow zones from mulitple zipcodes """
    compiled_grow_zones = []
    for zip_code in zipcode_model_list:
        compiled_grow_zones.append(zip_code.grow_zone)
    return compiled_grow_zones


def grow_zone_stripper(grow_zone):
    """ Strips brackets off grow zones """
    if ',' in grow_zone:
        grow_zone = grow_zone[1:-1]
        return grow_zone
    else:
        return grow_zone


def menu_parser(args):
    """ Parses user input data, checks if veg in
        database returns Django Produce model if found """
    arg_list = {arg.capitalize() for arg in args.split(' ')}
    produce = set()
    for arg in arg_list:
        produce.update([f.name for f in Produce.objects.filter(name=arg)])
    if len(produce) >= 1:
        produce = {i for i in produce}
        return produce
    else:
        return ["No recognized vegetables in local grow zone."]


def grow_zone_matcher(grow_zone):
    """ Returns produce in grow_zone(s) """
    produce = set()
    if len(grow_zone) > 1:
        grow_zone = grow_zone.replace(',', '')
        for i in grow_zone:
            produce.update([f.name for f in Produce.objects.filter(grow_zone__contains=i)])
    return produce
