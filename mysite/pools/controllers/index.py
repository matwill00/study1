from django.http import HttpResponse
from django.shortcuts import redirect, render
from pools.models import Resume
from pools.models import Gear_order


def index(request):
    return render(request, 'index.html', {})


def gears(request):
    return render(request, 'gears.html', {})


def rack_neck(request):
    return render(request, 'rack neck.html', {})


def worm_gears(request):
    return render(request, 'worm_gears.html', {})


def check(request):
    return render(request, 'check.html', {})


def resume(request):
    resume = Resume()
    resume.name = request.POST.get("name")
    resume.email = request.POST.get("email")
    resume.resume = request.POST.get("resume")
    resume.save()
    return redirect('/')


def gear_order(request):
    gear_order = Gear_order()
    gear_order.client_name = request.POST.get("client_name")
    gear_order.client_email = request.POST.get("client_email")
    gear_order.order_name = request.POST.get("order_name")
    gear_order.order_drawing = request.POST.get('order_drawing')
    gear_order.save()
    return redirect('/')
