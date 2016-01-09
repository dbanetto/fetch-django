from datetime import datetime, timedelta
import json

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from series.models import Series, MediaType
from series.forms import SeriesForm


def index(request):
    series = sorted(Series.objects.all(), key=lambda s: s.next_release() if type(s.next_release()) is datetime else datetime.max)

    if request.method == 'GET':
        filter = request.GET.get('filter')
        if filter:
            if filter == 'week':
                series = [s for s in series if type(s.next_release()) is datetime and \
                          s.next_release().date() <= (datetime.now().date() + timedelta(days=7))]

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
                                 .format(series.title))
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
                                     .format(series.title))
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
                             .format(series.title))
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

@csrf_exempt
def count(request, series_id):
    """
    Update a series current count if a valid change
    """
    series = get_object_or_404(Series, pk=series_id)
    if request.method == 'POST':
        try:
            try:
                print(request.body)
                body = json.loads(request.body.decode('utf-8'))
            except ValueError as e:
                return HttpResponse(json.dumps({'success': False, 'error': 'invalid json ' + str(e)}),
                                    content_type="application/json")
            if 'current_count' in body:
                current_count = int(body['current_count'])
                series.current_count = current_count
                series.clean()
                series.save()
                return HttpResponse(json.dumps({'success': True, 'current_count': series.current_count}),
                                    content_type="application/json")

            return HttpResponse(json.dumps({'success': False, 'error': 'no current_count'}),
                                content_type="application/json")
        except ValueError:
            return HttpResponse(json.dumps({'success': False, 'error': 'current count must be an int'}),
                                content_type="application/json")
        except Exception as e:
            return HttpResponse(json.dumps({'success': False, 'error': str(e)}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'current_count': series.current_count,
                                        'total_count': series.total_count}),
                            content_type="application/json")
