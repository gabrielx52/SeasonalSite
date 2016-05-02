from django.shortcuts import render
from seasonal.models import Produce, Location

# Create your views here.


def browse_view(request):
    produce = Produce.objects.order_by('-name')
    context = {'produce': produce}
    return render(request, 'browse.html', context)


def search_view(request):
    location = Location.objects.order_by('-name')
    produce = Produce.objects.order_by('-name')
    context = {'produce': produce, 'location': location}
    return render(request, 'search.html', context)
