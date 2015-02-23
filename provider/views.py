from django.shortcuts import render, get_object_or_404

from provider.models import Provider


def index(request):
    return render(request, 'provider/index.html',
                  {'providers': Provider.objects.all()})


def view(request, provider_id):
    provider = get_object_or_404(Provider, pk=provider_id)
    return render(request, 'provider/view.html',
                  {'provider': provider})
