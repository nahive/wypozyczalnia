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
from Wypoz.models import Pracownik
from Wypoz.models import Protokol
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from datetime import timedelta
from datetime import date
from django.db.models import Q

def home(request):
    all_entries = list(Auto.objects.all()[:5])
    return HttpResponse(render_to_response(
                                        'index.html',{'page':'main_page.html','user':request.user, 'car_entry':all_entries},
                                        ))

def cars_view(request):
    if request.method == 'POST':
        request.session['sel_car'] = request.POST.get('id_car','brak');
        return HttpResponseRedirect('/cars_reserve')

    all_entries = list(Auto.objects.filter(Q(num_dow = None) | Q(num_dow="")))
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
            cur_user = Klient.objects.get(login=req_user)
            num_dowodu = cur_user.num_dow
            sel_car.num_dow = num_dowodu
        except ObjectDoesNotExist:
            print("nie ma klienta")
        try:
            cur_user = Firma.objects.get(login=req_user)
            num_dowodu = cur_user.num_dow_p
            sel_car.num_dow = num_dowodu
        except ObjectDoesNotExist:
            print("nie ma firmy")
        if Auto.objects.filter(num_dow=num_dowodu).count() > 0:
            print(Auto.objects.filter(num_dow=num_dowodu).count())
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

def cars_give_back(request):
    req_user = request.user.username
    try:
        cur_user = Klient.objects.get(login=req_user)
        num_dowodu = cur_user.num_dow
    except ObjectDoesNotExist:
        print("nie ma w kl")
    try:
        cur_user = Firma.objects.get(login=req_user)
        num_dowodu = cur_user.num_dow_p
    except ObjectDoesNotExist:
        print("nie ma w fir")
    try:
        cur_user = Pracownik.objects.get(login=req_user)
        return HttpResponseRedirect('/cars_take_view')
    except ObjectDoesNotExist:
        print("nie ma w prac")
    if Auto.objects.filter(num_dow=num_dowodu).count() > 0:
        try: 
            car = Auto.objects.get(num_dow=num_dowodu)
            car.do_odd = "True"
            car.save()
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/cars_give_fail')
        return HttpResponseRedirect('/cars_give_success')
    return HttpResponseRedirect('/cars_give_fail')

def cars_give_success(request):
       return HttpResponse(render_to_response(
                                            'index.html',{'page':'cars_give_success.html','user':request.user},
                                           ))
def cars_give_fail(request):
    return HttpResponse(render_to_response(
                                    'index.html',{'page':'cars_give_fail.html','user':request.user},
                                   ))
def cars_take_view(request):
    if request.method == 'POST':
        request.session['take_car'] = request.POST.get('id_car','brak');
        return HttpResponseRedirect('/cars_take_protocol')

    all_entries = list(Auto.objects.filter(do_odd = True))
    c = {'page':'cars_take_view.html','user':request.user, 'car_entry':all_entries}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def cars_take_protocol(request):  #sprawdzac czy juz nie wypozyczylismy samochodu
    if request.method== 'POST':
            samochodp = request.session['take_car']
            try:
                samochodq = Auto.objects.get(id=samochodp)
                samochod_cena = samochodq.cena
                samochod_dni = datetime.now().date() - samochodq.data_wyp
                samochod_wycena = int(samochod_cena) * int(samochod_dni.days) 
                samochodq.data_odd = None
                samochodq.data_wyp = None
                samochodq.num_dow = None
                samochodq.do_odd = False
                samochodq.save()
            except ObjectDoesNotExist:
                print("to nie auto")
            numdow = request.POST.get('client','')
            datep = datetime.now()
            opisp = request.POST.get('desc','')
            cena_dodat = request.POST.get('price','')
            samochod_final_cena = int(cena_dodat) + int(samochod_wycena)
            try:
                cli = Klient.objects.get(num_dow=numdow)
                loginp = cli.login
                protocol = Protokol(samochod = samochodq, klient = cli,data=datep,opis=opisp,wycena=samochod_final_cena)
            except ObjectDoesNotExist:
                print("to nie klient")
            try:
                cli = Firma.objects.get(num_dow_p=numdow)
                loginp = cli.login
                protocol = Protokol(samochod = samochodp, firma=cli,data=datep,opis=opisp,wycena=samochod_final_cena)
            except ObjectDoesNotExist:
                print("to nie firma")
            protocol.save()
            return HttpResponseRedirect('/cars_take_success')

    take_car = request.session['take_car']
    taken_car = Auto.objects.get(id=take_car)
    c = {'page':'cars_take_protocol.html','user':request.user, 'o':taken_car, 'dow':taken_car.num_dow, 'data_odd':taken_car.data_odd}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def cars_take_success(request):
    sel_id = request.session['take_car']
    sel_car = Auto.objects.get(id=sel_id)
    return HttpResponse(render_to_response(
                                            'index.html',{'page':'cars_take_success.html','user':request.user, 'o':sel_car},
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
    return HttpResponse(render_to_response('index.html',
                              {'page':'main_page.html','user': request.user}))

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
           
            klient = Klient(login = loginp, haslo = haslop, imie = imiep, naz = nazwiskop, miasto = miastop, ulica = ulicap, tel = telefonp, num_dow = nr_dowodu_osobistegop, pesel = peselp, email = mailp)
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
            firma = Firma(login = loginp, haslo = haslop,naz_pel = nazwadl, naz_skr = nazwakr, nip = nipp, reg = regonp, rodz_dzial = rodzajdz, num_dow_p = nr_dowodu_osobistegop, imie_p = imiep, naz_p = nazwiskop)
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
