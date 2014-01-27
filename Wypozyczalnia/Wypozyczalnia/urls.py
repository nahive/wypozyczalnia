from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',url(r'^$', 'Wypoz.views.home', name='home'),
                       url(r'^register/','Wypoz.views.register'), 
                       url(r'^register_success/','Wypoz.views.register_success'),
                       url(r'^view_cars/', 'Wypoz.views.cars_view'), 
                       url(r'^main/', 'Wypoz.views.home'),
                       url(r'^cars_reserve/','Wypoz.views.cars_reserve'),
                       url(r'^login/','Wypoz.views.login'),
                       url(r'^auth/$', 'Wypoz.views.auth_view'),
                       url(r'^login_me/$', 'Wypoz.views.login_user'),
                       url(r'^logout_me/$', 'Wypoz.views.logout_user'),
                       url(r'^invalid/$', 'Wypoz.views.invalid_login'),
                       url(r'^cars_reserve_success/', 'Wypoz.views.cars_reserve_success'),
                       url(r'^cars_reserve_fail/','Wypoz.views.cars_reserve_fail'),
                       url(r'^give_back/','Wypoz.views.cars_give_back'),
                       url(r'^cars_give_success/', 'Wypoz.views.cars_give_success'),
                       url(r'^cars_give_fail/','Wypoz.views.cars_give_fail'),
                       url(r'^cars_take_success/', 'Wypoz.views.cars_take_success'),
                       url(r'^cars_take_protocol/', 'Wypoz.views.cars_take_protocol'),
                       url(r'^cars_take_view/', 'Wypoz.views.cars_take_view'),

    # Examples:
    # url(r'^$', 'Wypozyczalnia.views.home', name='home'),
    # url(r'^Wypozyczalnia/', include('Wypozyczalnia.Wypozyczalnia.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
