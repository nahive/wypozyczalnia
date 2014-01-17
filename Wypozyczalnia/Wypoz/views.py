# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    return HttpResponse(render_to_response(
                                        'index.html',{'page':'main_page.html'},
                                        ))
def login(request):
    return HttpResponse(render_to_response(
                                        'index.html',{'page':'login.html'},
                                        ))

def register(request):
    return HttpResponse(render_to_response(
                                         'index.html',{'page':'register.html'},
                                         ))

def cars_view(request):
    return HttpResponse(render_to_response(
                                           'index.html',{'page':'cars_view.html'},
                                           ))

def cars_reserve(request):
    return HttpResponse(render_to_response(
                                           'index.html',{'page':'cars_reserve.html'},
                                           ))