"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from django.conf import settings
from django.test.client import Client
from django.utils.importlib import import_module
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from Wypoz.models import *
from Wypoz.views import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/cars_view')
        # Recall that middleware are not suported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user
        # Test my_view() as if it were deployed at /customer/details
        response = cars_view(request)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)


class PracownikTestCase(TestCase):
    def setUp(self):
        Pracownik.objects.create(login="SnoopZilla", haslo="Weed", data_ur='2000-01-01')

    def test_pracownik_odbierz(self):
        """Sprawdza poprawnosc metody odbierz"""
        snoop = Pracownik.objects.get(login="SnoopZilla")
        self.assertEqual(snoop.odbierz(), 1)

    def test_pracownik_login(self):
        """Sprawdza poprawnosc metody odbierz"""
        snoop = Pracownik.objects.get(login="SnoopZilla")
        self.assertEqual(snoop.login, "SnoopZilla")


#class SessionTestCase(TestCase):
#    def setUp(self):
#        # Every test needs access to the request factory.
#        self.factory = RequestFactory()
#        self.user = User.objects.create_user(
#            username='jacob', password='top_secret')

#        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
#        engine = import_module(settings.SESSION_ENGINE)
#        store = engine.SessionStore()
#        store.save()
#        self.session = store
#        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
#        self.session['sel_car'] = 1
#        #session = self.session
#        #session['sel_car'] = 'G'
#        #session.save()


#    def test_cars_view(self):
#        # Create an instance of a GET request.
#        request = self.factory.get('')
#        # Recall that middleware are not suported. You can simulate a
#        # logged-in user by setting request.user manually.
#        request.user = self.user
#        # Test my_view() as if it were deployed at /customer/details
#        response = cars_view(request)
#        self.assertEqual(response.status_code, 200)

#    def test_cars_reserve(self):
#        session = self.session
#        session['sel_car'] = 'G'
#        session.save()
#        request = self.factory.get('')
#        request.user = self.user
#        response = cars_reserve(request)
#        self.assertEqual(response.status_code, 200)

##class BlahTestCase(SessionTestCase):

##    def test_blah_with_session(self):
##        session = self.session
##        session['operator'] = 'G'
##        session.save()

#class Test(TestCase):
#    def setUp(self):
#        self.factory = RequestFactory()
#        self.user = User.objects.create_user(
#            username='jacob', password='top_secret')
#        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
#        engine = import_module('django.contrib.sessions.backends.file')
#        store = engine.SessionStore()
#        store.save()

#        self.client = Client()
#        self.session = store
#        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

#    def test_exception_no_next_stage(self):
#        session = self.session
#        session['sel_car'] = 'bar'
#        session.save()

#        #response = self.client.get('/cars_reserve')
#        request = self.factory.get('/cars_reserve')
#        request.user = self.user
#        request.session['sel_car'] = '1'
#        response = cars_reserve(request)
#        self.assertEqual(response.status_code, 200)

#        #session_data = session.load()
#        #self.assertEqual(session_data['sel_car'], 'baz')

