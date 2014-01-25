from django.contrib import admin
from Wypoz.models import *
from django.contrib.auth.models import User

#admin.site.register(Auto)
#admin.site.register(Pracownik)
#admin.site.register(Protokol)
#admin.site.register(Klient)
#admin.site.register(Firma)

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_rej', 'marka', 'model')

class PracownikAdmin(admin.ModelAdmin):
    list_display = ('login', 'imie', 'naz')

class ProtokolAdmin(admin.ModelAdmin):
    list_display = ('id', 'samochod', 'klient', 'firma')

class KlientAdmin(admin.ModelAdmin):
    list_display = ('login', 'imie', 'naz')

class FirmaAdmin(admin.ModelAdmin):
    list_display = ('login', 'reg', 'naz_pel')

admin.site.register(Auto, AutoAdmin)
admin.site.register(Pracownik, PracownikAdmin)
admin.site.register(Protokol, ProtokolAdmin)
admin.site.register(Klient, KlientAdmin)
admin.site.register(Firma, FirmaAdmin)