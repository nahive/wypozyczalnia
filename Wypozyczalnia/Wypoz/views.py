# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from Wypoz.forms import ClientRegistrationForm


def home(request):
    return HttpResponse(render_to_response(
                                        'index.html',{'page':'main_page.html','user':request.user},
                                        ))

def cars_view(request):
    return HttpResponse(render_to_response(
                                           'index.html',{'page':'cars_view.html','user':request.user},
                                           ))

def cars_reserve(request):
    return HttpResponse(render_to_response(
                                           'index.html',{'page':'cars_reserve.html','user':request.user},
                                           ))

def login(request):
    c = {'page':'login.html', 'user':request.user}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/login_me')
    else:
        return HttpResponseRedirect('/invalid')

def login_user(request):
    return render_to_response('index.html',
                              {'page':'cars_view.html','user': request.user})

def logout_user(request):
    auth.logout(request)
    return render_to_response('index.html',{'page':'main_page.html','user':request.user})

def invalid_login(request):
    return render_to_response('index.html',{'page':'invalid.html','user':request.user})

def register(request):
    return HttpResponse(render_to_response(
                                         'index.html',{'page':'register.html','user':request.user},
                                         ))
def register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')

    args = {}
    args.update(csrf(request))

    args['form'] = ClientRegistrationForm()
    return render_to_response('register.html',args) 
                                                    # return render_to_response('register.html',args)
                                                    # poprawic tutaj jeszcze, bo jest standardowy form
                                                    # http://www.youtube.com/watch?v=xaPHSlTmg1s

def register_success(request):
    return render_to_response('index.html',{'page':'register_success.html','user':request.user})