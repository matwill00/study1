from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def gears(request):
    return render(request, 'gears.html', {})


def rack_neck(request):
    return render(request, 'rack neck.html', {})


def worm_gears(request):
    return render(request, 'worm_gears.html', {})
