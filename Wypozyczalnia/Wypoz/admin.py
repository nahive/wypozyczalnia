from django.contrib import admin
from Wypoz.models import *

#admin.site.register(Auto)
admin.site.register(Pracownik)
admin.site.register(Protokol)
admin.site.register(Klient)
admin.site.register(Firma)

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_rej')

admin.site.register(Auto, AutoAdmin)