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

def login_user(request):
    state = "Log in"
    username = password = ' '
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                state = "Success!"
            else:
                state = "Not active!"
        else:
            state = "Incorrect!"
    return render_to_resonse('index.html',RequestContext(request,{'page':'cars_view.html','state':state}),
                             )