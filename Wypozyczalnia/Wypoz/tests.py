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
from django.core.urlresolvers import reverse 
from Wypoz.views import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """ Tests that 1 + 1 always equals 2. """
        self.assertEqual(1 + 1, 2)

class SimpleRequest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email = 'temporary@gmail.com', password='top_secret')

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
        response = c.post('/login/', {'username': 'jacob', 'password': 'top_secret'})
        self.assertEqual(response.status_code, 200)

    def test_is_authenticated(self):
        self.assertEqual(self.user.is_authenticated(), True)

class SimpleClient(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Shepard', email = 'shepard@gmail.com', password='Normandy')

    def testLogin(self):
        self.client.login(username='Shepard', password='Normandy')
        response = self.client.get('/invalid/', follow=True)
        self.assertEqual(response.status_code, 200)

class PracownikTestCase(TestCase):
    def setUp(self):
        Pracownik.objects.create(login="SnoopZilla", haslo="Weed", data_ur='2000-01-01')

    def test_pracownik_odbierz(self):
        """ Sprawdza poprawnosc metody odbierz """
        snoop = Pracownik.objects.get(login="SnoopZilla")
        self.assertEqual(snoop.odbierz(), 1)

    def test_pracownik_login(self):
        snoop = Pracownik.objects.get(login="SnoopZilla")
        self.assertEqual(snoop.login, "SnoopZilla")
