from django.http import HttpResponse
from django.shortcuts import redirect, render
from pools.models import Resume, Gear_order, Rack_neck_order, Worm_gear_order


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
    gear_order.order_drawing = request.FILES['order_drawing']
    gear_order.save()
    return redirect('/')


def rack_neck_order(request):
    rack_neck_order = Rack_neck_order()
    rack_neck_order.client_name = request.POST.get("client_name")
    rack_neck_order.client_email = request.POST.get("client_email")
    rack_neck_order.order_name = request.POST.get("order_name")
    rack_neck_order.order_drawing = request.FILES['order_drawing']
    rack_neck_order.save()
    return redirect('/')


def worm_gear_order(request):
    worm_gear_order = Worm_gear_order()
    worm_gear_order.client_name = request.POST.get("client_name")
    worm_gear_order.client_email = request.POST.get("client_email")
    worm_gear_order.order_name = request.POST.get("order_name")
    worm_gear_order.order_drawing = request.FILES['order_drawing']
    worm_gear_order.save()
    return redirect('/')
