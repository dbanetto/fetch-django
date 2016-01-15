from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from fetcher import api

import requests
import json

def index(request):
    return render(request, 'fetcher/index.html',
                  {'result': api.status()})

def status(request):
    if request.method == 'GET' and request.META.get('CONTENT_TYPE') == 'application/json':
        return HttpResponse(json.dumps(api.status()), content_type='application/json')
    else:
        return HttpResponseRedirect(reverse('fetcher:index'))

@csrf_exempt
def force_fetch(request):
    if request.method == 'POST' and request.META.get('CONTENT_TYPE') == 'application/json':
        return HttpResponse(json.dumps(api.force_fetch()), content_type='application/json')
    else:
        return HttpResponseRedirect(reverse('fetcher:index'))

@csrf_exempt
def force_sort(request):
    if request.method == 'POST' and request.META.get('CONTENT_TYPE') == 'application/json':
        return HttpResponse(json.dumps(api.force_sort()), content_type='application/json')
    else:
        return HttpResponseRedirect(reverse('fetcher:index'))

