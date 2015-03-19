from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from provider.models import Provider, BaseProvider
from provider.forms import ProviderForm


def index(request):
    providers = Provider.objects.all()
    if request.META.get('CONTENT_TYPE') == 'application/json':
        return render(request, 'provider/index.json',
                      {'providers': providers},
                      content_type='application/json')
    else:
        return render(request, 'provider/index.html',
                      {'providers': providers})


def view(request, provider_id):
    provider = get_object_or_404(Provider, pk=provider_id)
    return render(request, 'provider/view.html',
                  {'provider': provider})


def new(request):
    form = ProviderForm()
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        form.full_clean()
        if form.is_valid():
            new_provider = form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "<strong>Success</strong> Created {}"
                                 .format(new_provider.name))
            return HttpResponseRedirect(reverse('provider:view',
                                                args=[new_provider.id]))
    else:
        return render(request, 'provider/new.html',
                      {'form': form})


def edit(request, provider_id):
    provider = get_object_or_404(Provider, pk=provider_id)
    form = ProviderForm(instance=provider)
    if request.method == 'POST':
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            if form.has_changed():
                form.save()

                messages.add_message(request,
                                     messages.SUCCESS,
                                     "<strong>Success</strong> Edited {}"
                                     .format(provider.name))
            return HttpResponseRedirect(reverse('provider:view',
                                                args=[provider.id]))
    return render(request, 'provider/edit.html',
                  {'form': form,
                   'provider': provider})


def delete(request, provider_id):
    if request.method == 'POST':
        provider = get_object_or_404(Provider, pk=provider_id)
        messages.add_message(request,
                             messages.INFO,
                             "{} has been deleted"
                             .format(provider.name))
        provider.delete()
        return HttpResponseRedirect(reverse('provider:index'))
    else:
        return HttpResponseRedirect(reverse('provider:view',
                                            args=(provider_id)))


def base_index(request):
    if request.META.get('CONTENT_TYPE') == 'application/json':
        return render(request, 'provider/base_index.json',
                      {'base_providers': BaseProvider.objects.all()},
                      content_type='application/json')
    else:
        return render(request, 'provider/base_index.html',
                      {'base_providers': BaseProvider.objects.all()})


def base_view(request, base_provider_id):
    base_provider = get_object_or_404(BaseProvider, pk=base_provider_id)
    if request.META.get('CONTENT_TYPE') == 'application/json':
        return render(request, 'provider/base_view.json',
                      {'base_provider': base_provider},
                      content_type='application/json')
    else:
        return render(request, 'provider/base_view.html',
                      {'base_provider': base_provider})
