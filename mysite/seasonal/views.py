from django.shortcuts import render
from seasonal.models import Produce, Location
from .forms import AllForm
from .functions import local_zipcodes, grow_zone_stripper, grow_zone_matcher, menu_parser, multi_zipcode_growzone_compiler, local_zipcodes_models

# Create your views here.


def home_view(request):
    if request.method == 'GET':
        form = AllForm(request.GET)
        if form.is_valid():
            zipcode = form.cleaned_data['zipcode']
            distance = form.cleaned_data['distance']
            produce = form.cleaned_data['produce']
            location_model = Location.objects.get(zipcode=zipcode)
            grow_zone = grow_zone_stripper(location_model.grow_zone)
            #zips_in_radius = local_zipcodes(zipcode, int(distance))
            zips_in_radius = local_zipcodes_models(zipcode, int(distance))
            growzones_in_radius = multi_zipcode_growzone_compiler(zips_in_radius)
            city, state = str(location_model).split(',')
            city = city.capitalize()
            starting_location = city.capitalize() + ' ' + state
            local_produce = grow_zone_matcher(grow_zone)
            parsed_veg_args = menu_parser(produce)
            if produce == "":
                """ if produce list is blank will redirect to
                    show grow zone and produce in same zone """
                context = {'zipcode': zipcode,
                           'distance': distance,
                           'zips_in_radius': zips_in_radius,
                           'starting_location': starting_location,
                           'grow_zone': grow_zone,
                           'location_model': location_model,
                           'local_produce': local_produce,
                           'city': city,
                           'state': state}
                return render(request, 'local_grow.html', context)
            else:
                context = {'zipcode': zipcode,
                           'distance': distance,
                           'produce': produce,
                           'zips_in_radius': zips_in_radius,
                           'starting_location': starting_location,
                           'city': city,
                           'state': state,
                           'grow_zone': grow_zone,
                           'parsed_veg_args': parsed_veg_args,
                           'growzones_in_radius': growzones_in_radius}
            return render(request, 'local_harvest.html', context)
    form = AllForm()
    return render(request, 'home.html', {'form': form})


def browse_produce_view(request):
    produce = Produce.objects.order_by('name')
    context = {'produce': produce}
    return render(request, 'browse_produce.html', context)


def browse_locations_view(request):
    locations = Location.objects.order_by('state')
    context = {'locations': locations}
    return render(request, 'browse_locations.html', context)


def search_view(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        else:
            produce = Produce.objects.filter(name__icontains=q)

            if produce:
                context = {'produce': produce, 'query': q}
                return render(request, 'search_results.html', context)
            else:
                errors.append('No search results found for: {}'.format(q))
    return render(request, 'search.html', {'errors': errors})


def faq_view(request):
    return render(request, 'faq.html')
