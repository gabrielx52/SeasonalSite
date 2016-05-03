from django.shortcuts import render
from seasonal.models import Produce, Location

# Create your views here.


def browse_view(request):
    produce = Produce.objects.order_by('-name')
    context = {'produce': produce}
    return render(request, 'browse.html', context)


def search_view(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            produce = Produce.objects.filter(name__icontains=q)
            context = {'produce': produce, 'query': q}
            return render(request, 'search_results.html', context)
    return render(request, 'search.html', {'error': error})