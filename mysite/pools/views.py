from django.http import HttpResponse


def index(f):
    return HttpResponse('hey')

