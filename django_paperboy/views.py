# import ipdb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django_paperboy.models import Paperboy


def home_page(request):
    paperboys = Paperboy.objects.all()
    total_earned = Paperboy.total_earned()
    total_delivered = Paperboy.total_delivered()
    context = {'paperboys': paperboys, 'total_earned': total_earned, 'total_delivered': total_delivered}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def paperboy(request, id):
    paperboy = get_object_or_404(Paperboy, pk=id)
    context = {'paperboy': paperboy}
    response = render(request, 'paperboy.html', context)
    return HttpResponse(response)


def home_page_redirect(request):
    return redirect(home_page)


def deliver(request):
    # ipdb.set_trace()
    paperboy_num = request.POST['boy_id']
    start_address = int(request.POST['start-address'])
    end_address = int(request.POST['end-address'])
    paperboy = Paperboy.objects.get(pk=paperboy_num)
    paperboy.deliver(start_address, end_address)
    return redirect(home_page)
