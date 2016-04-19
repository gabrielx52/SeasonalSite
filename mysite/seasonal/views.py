from django.shortcuts import render
from seasonal.models import Produce

# Create your views here.


def browse_view(request):
    produce = Produce.objects.order_by('-name')
    context = {'produce': produce}
    return render(request, 'browse.html', context)
