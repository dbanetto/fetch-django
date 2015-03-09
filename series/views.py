from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from series.models import Series

def index(request):
    series = Series.objects.all()
    return render(request, 'series/index.html',
                  {'series': series})


def view(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    return render(request, 'series/view.html',
                  {'series': series})


def new(request):
    return render(request, 'series/index.html')


def edit(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    return render(request, 'series/view.html',
                  {'series': series})


def delete(request, series_id):
    if request.method == 'POST':
        series = get_object_or_404(Series, pk=series_id)
        messages.add_message(request,
                             messages.INFO,
                             "{} has been deleted"
                             .format(series.name))
        # series.delete() FIXME
        return HttpResponseRedirect(reverse('series:index'))
    else:
        return HttpResponseRedirect(reverse('series:view',
                                            args=(series_id)))
