from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',url(r'^$', 'Wypoz.views.home', name='home'),
                       url(r'^login/','Wypoz.views.login'),
                       url(r'^register/','Wypoz.views.register'), 
                       url(r'^view_cars/', 'Wypoz.views.cars_view'), 
                       url(r'^main/', 'Wypoz.views.home'),
                       url(r'^cars_reserve/','Wypoz.views.cars_reserve'),
    # Examples:
    # url(r'^$', 'Wypozyczalnia.views.home', name='home'),
    # url(r'^Wypozyczalnia/', include('Wypozyczalnia.Wypozyczalnia.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
