from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from seasonal.models import Produce, Location

from .forms import AllForm, ZipCodeForm, ProduceForm, DistanceForm, ContactForm
from .functions import grow_zone_stripper, grow_zone_matcher, menu_parser, multi_zipcode_growzone_compiler, local_zipcodes_models


# Create your views here.


def home_view(request):
    """ Home page view """
    z_form = ZipCodeForm()
    d_form = DistanceForm()
    p_form = ProduceForm()
    if request.method == 'GET':
        form = AllForm(request.GET)
        if form.is_valid():
            zipcode = form.cleaned_data['zipcode']
            distance = form.cleaned_data['distance']
            produce = form.cleaned_data['produce']
            try:
                location_model = Location.objects.get(zipcode=zipcode)
                grow_zone = grow_zone_stripper(location_model.grow_zone)
                zips_in_radius = local_zipcodes_models(zipcode, int(distance))
                growzones_in_radius = multi_zipcode_growzone_compiler(zips_in_radius)
                city, state = str(location_model).split(',')
                city = city.capitalize()
                starting_location = city.capitalize() + ' ' + state
                local_produce = grow_zone_matcher(grow_zone)
                parsed_veg_args = menu_parser(produce)
            except:
                not_found = "Not a recognized zipcode"
                context = {'form': form,
                           'z_form': z_form,
                           'd_form': d_form,
                           'p_form': p_form,
                           'zipcode': zipcode,
                           'not_found': not_found}
                return render(request, 'home.html', context)
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
    context = {'z_form': z_form,
               'd_form': d_form,
               'p_form': p_form}
    return render(request, 'home.html', context)


def browse_produce_view(request):
    """ Browse produce database """
    produce_list = Produce.objects.order_by('name')
    paginator = Paginator(produce_list, 10) # Show 10 produce items per page.
    page = request.GET.get('page')

    try:
        produce = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        produce = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        produce = paginator.page(paginator.num_pages)

    context = {'produce': produce}
    return render(request, 'browse_produce.html', context)


def browse_locations_view(request):
    """ Browse location database """
    location_list = Location.objects.order_by('state')
    context = get_paged_browse_context(request, location_list)
    return render(request, 'browse_locations.html', context)


def search_view(request):
    """ Search through produce database """
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
    """ FAQ """
    return render(request, 'faq.html')


def contact_view(request):
    """ Contact page """
    email_sent = False
    errors = []
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            contact_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']
            try:
                # TODO: Add real email address.
                send_mail(subject, message, contact_email, ['admin@gmail.com'])
                email_sent = True
            except Exception as e:
                # TODO: Add better exception handling.
                errors.append(e)
    context = {'form': form, 'email_sent': email_sent, 'errors': errors}
    return render(request, 'contact.html', context)


def get_paged_browse_context(request, queryset):
    """ Splits browse to pages of 10 items """
    paginator = Paginator(queryset, 10)  # Show 10 contacts per page
    if request.GET.get('page'):
        try:
            requested_page = request.GET.get('page')
        except PageNotAnInteger:
            requested_page = 1
        except EmptyPage:
            requested_page = paginator.num_pages
    else:
        requested_page = 1
    results = paginator.page(requested_page)
    min_page = int(requested_page) - 4
    max_page = int(requested_page) + 4

    return {'results': results, 'min': min_page, 'max': max_page}
