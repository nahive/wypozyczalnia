# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from Wypoz.forms import ClientRegistrationForm
from Wypoz.models import Auto
from Wypoz.models import Klient
from Wypoz.models import Firma
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from datetime import timedelta

def home(request):
    all_entries = list(Auto.objects.all()[:5])
    return HttpResponse(render_to_response(
                                        'index.html',{'page':'main_page.html','user':request.user, 'car_entry':all_entries},
                                        ))

def cars_view(request):
    if request.method == 'POST':
        request.session['sel_car'] = request.POST.get('id_car','brak');
        return HttpResponseRedirect('/cars_reserve')

    all_entries = list(Auto.objects.filter(num_dow = ''))
    c = {'page':'cars_view.html','user':request.user, 'car_entry':all_entries}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def cars_reserve(request):  #sprawdzac czy juz nie wypozyczylismy samochodu
    if request.method== 'POST':
        req_user = request.user.username
        dayss = request.POST.get('days','')
        sel_id = request.session['sel_car']
        sel_car = Auto.objects.get(id=sel_id)
        sel_car.data_wyp = datetime.now()
        sel_car.data_odd = datetime.now() + timedelta(days=int(dayss))
        try:
            cur_user = Klient.objects.get(nick=req_user)
            num_dowodu = cur_user.num_dow
            sel_car.num_dow = num_dowodu
        except ObjectDoesNotExist:
            print "nie ma"
        try:
            cur_user = Firma.objects.get(nick=req_user)
            num_dowodu = cur_user.num_dow_p
            sel_car.num_dow = num_dowodu
        except ObjectDoesNotExist:
            print "nie ma"
        if Auto.objects.filter(num_dow=num_dowodu).count != 0:
            return HttpResponseRedirect('/cars_reserve_fail')
        sel_car.save()
        return HttpResponseRedirect('/cars_reserve_success')

    sel_id = request.session['sel_car']
    sel_car = Auto.objects.get(id=sel_id)
    c = {'page':'cars_reserve.html','user':request.user, 'o':sel_car}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def cars_reserve_success(request):
    sel_id = request.session['sel_car']
    sel_car = Auto.objects.get(id=sel_id)
    return HttpResponse(render_to_response(
                                            'index.html',{'page':'cars_reserve_success.html','user':request.user, 'o':sel_car},
                                           ))

def cars_reserve_fail(request):
       return HttpResponse(render_to_response(
                                            'index.html',{'page':'cars_reserve_fail.html','user':request.user},
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
    if request.method == 'POST':
        czy = request.POST.get('fizyczna','')
        czy2 = request.POST.get('firma','')
        if czy == 'osoba fizyczna':
            imiep = request.POST.get('imie','')
            nazwiskop = request.POST.get('nazwisko','')
            ulicap = request.POST.get('ulica','')
            miastop = request.POST.get('miasto','')
            peselp = request.POST.get('pesel','')
            telefonp = request.POST.get('telefon','')
            nr_dowodu_osobistegop = request.POST.get('nr_dowodu_osobistego','')
            loginp = request.POST.get('login','')
            haslop = request.POST.get('haslo','')
            mailp = request.POST.get('email','')
           
            klient = Klient(nick = loginp, haslo = haslop, imie = imiep, naz = nazwiskop, miasto = miastop, ulica = ulicap, tel = telefonp, num_dow = nr_dowodu_osobistegop, pesel = peselp, email = mailp)
            klient.save()
            user = User(username = loginp)
            user.set_password(haslop)
            user.save()

            return HttpResponseRedirect('/register_success')

        elif czy2 == 'firma':
            nazwadl = request.POST.get('nazwa')
            nazwakr = request.POST.get('nazwa_skr')
            imiep = request.POST.get('imie','')
            nazwiskop = request.POST.get('nazwisko','')
            nr_dowodu_osobistegop = request.POST.get('nr_dowodu_osobistego','')
            loginp = request.POST.get('login','')
            haslop = request.POST.get('haslo','')
            mailp = request.POST.get('email','')
            rodzajdz = request.POST.get('rodzaj','')
            nipp = request.POST.get('nip','')
            regonp = request.POST.get('regon','')
            firma = Firma(nick = loginp, haslo = haslop,naz_pel = nazwadl, naz_skr = nazwakr, nip = nipp, reg = regonp, rodz_dzial = rodzajdz, num_dow_p = nr_dowodu_osobistegop, imie_p = imiep, naz_p = nazwiskop)
            firma.save()
            user = User(username = loginp, password = haslop)
            user.set_password(haslop)
            user.save()
            return HttpResponseRedirect('/register_success')

    c = {'page': 'register.html', 'user': request.user}
    c.update(csrf(request))

    return render_to_response('index.html',c) 
                                                    # return render_to_response('register.html',args)
                                                    # tylko nie wiem czy jest rejestracja w naszych wybranych przypadkach ;d
                                                    # poprawic tutaj jeszcze, bo jest standardowy form
                                                    # http://www.youtube.com/watch?v=xaPHSlTmg1s

def register_success(request):
    return render_to_response('index.html',{'page':'register_success.html','user':request.user})
