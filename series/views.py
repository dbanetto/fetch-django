from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from series.models import Series, MediaType
from series.forms import SeriesForm


def index(request):
    series = Series.objects.all()
    if request.META.get('CONTENT_TYPE') == 'application/json':
        return render(request, 'series/index.json',
                      {'series': series},
                      content_type='application/json')
    else:
        return render(request, 'series/index.html',
                      {'series': series})


def view(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    return render(request, 'series/view.html',
                  {'series': series})


def new(request):
    form = SeriesForm()
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            series = form.save(commit=False)
            if 'poster' in request.FILES:
                series.poster = request.FILES['poster']
            series.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "<strong>Success</strong> Created {}"
                                 .format(series.name))
            return HttpResponseRedirect(reverse('series:view',
                                        args=[series.id]))

    return render(request, 'series/new.html',
                  {'form': form})


def edit(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    form = SeriesForm(instance=series)
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES, instance=series)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.add_message(request,
                                     messages.SUCCESS,
                                     "<strong>Success</strong> Edited {}"
                                     .format(series.name))
            return HttpResponseRedirect(reverse('series:view',
                                                args=[series.id]))
    return render(request, 'series/edit.html',
                  {'series': series,
                   'form': form})


def delete(request, series_id):
    if request.method == 'POST':
        series = get_object_or_404(Series, pk=series_id)
        messages.add_message(request,
                             messages.INFO,
                             "{} has been deleted"
                             .format(series.name))
        series.delete()
        return HttpResponseRedirect(reverse('series:index'))
    else:
        return HttpResponseRedirect(reverse('series:view',
                                            args=(series_id)))


def media_type_index(request):
    if request.META.get('CONTENT_TYPE') == 'application/json':
        return render(request, 'series/media_index.json',
                      {'media_types': MediaType.objects.all()},
                      content_type='application/json')
    return render(request, 'series/media_index.html',
                  {'media_types': MediaType.objects.all()})


def media_type_view(request, media_type_id):
    media_type = get_object_or_404(MediaType, pk=media_type_id)
    if request.META.get('CONTENT_TYPE') == 'application/json':
        return render(request, 'series/media_view.json',
                      {'media_type': media_type},
                      content_type='application/json')
    return render(request, 'series/media_view.html',
                  {'media_type': media_type})
