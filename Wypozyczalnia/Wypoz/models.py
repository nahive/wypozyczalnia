from django.db import models

# Create your models here.
class Auto(models.Model):
    IdSamochodu = models.CharField(max_length=200)
    Marka = models.CharField(max_length=200)
    Model = models.CharField(max_length=200)
    Klasa = models.CharField(max_length=200)
    NumerRej = models.CharField(max_length=200)
    Wyposaz = models.CharField(max_length=200)
    Silnik = models.CharField(max_length=200)
    Kolor = models.CharField(max_length=200)
    LiczbaSiedz = models.CharField(max_length=200)
    Cena = models.CharField(max_length=200)
    TerminWyp = models.CharField(max_length=200)
    TerminOdd = models.CharField(max_length=200)
    NrDowodu = models.CharField(max_length=200)

class Pracownik(models.Model):
    Imie = models.CharField(max_length=200)
    Nazwisko = models.CharField(max_length=200)
    Ulica = models.CharField(max_length=200)
    Miasto = models.CharField(max_length=200)
    DataUr = models.CharField(max_length=200)
    NrDowoduPrac = models.CharField(max_length=200)

    def odbierz():
        return 1

class Protokol(models.Model):
    IdSam = models.CharField(max_length=200)
    IdProt = models.CharField(max_length=200)
    NrDow = models.CharField(max_length=200)
    Data = models.CharField(max_length=200)
    Opis = models.CharField(max_length=200)
    Wycena = models.CharField(max_length=200)

