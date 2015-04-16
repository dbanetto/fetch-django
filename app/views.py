
from datetime import datetime, timedelta
import json

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from series.models import Series

def index(request):
    series = []
    for s in Series.objects.all():
        next = s.next_release()
        if next is not None and next < datetime.now() + timedelta(days=7):
            series.append(s)
    series.sort(key=lambda s: s.next_release() if type(s.next_release()) is datetime else datetime.max)

    return render(request, 'app/index.html',
                  {'series_week': series})
