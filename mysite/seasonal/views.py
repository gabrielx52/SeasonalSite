from django.shortcuts import render
from seasonal.models import Produce, Location

# Create your views here.


def home_view(request):
    context = {}
    return render(request, 'home.html', context)


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
