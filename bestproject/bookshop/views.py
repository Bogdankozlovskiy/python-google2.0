from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger('django')


def hello(request):
    logger.error('hello error')
    return HttpResponse("<h2>hello from django</h2>")


def world(request):
    response = {}
    response['name'] = "Egor"
    response['users'] = ["Pavel", "Eugen", "Hajima", "Gaben"]
    return render(request, './bookshop/index.html', response)
