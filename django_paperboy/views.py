from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django_paperboy.models import Paperboy


def home_page(request):
    paperboys = Paperboy.objects.all()
    context = {'paperboys': paperboys}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def paperboy(request, id):
    paperboy = get_object_or_404(Paperboy, pk=id)
    context = {'paperboy': paperboy}
    response = render(request, 'paperboy.html', context)
    return HttpResponse(response)


def home_page_redirect(request):
    return redirect(home_page)
