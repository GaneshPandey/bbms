from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from blood_donor_info.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',direct_to_template,{'template':'index.html'},'index'),
    (r'^events/',include('events.urls')),
    (r'^donorinfo/',include('blood_donor_info.urls')),
    (r'^donorfinder/$',include('donorfinder.urls')),
    (r'^login/$',signin),
    (r'^logout/$',signout),
    (r'^about/$',direct_to_template,{'template':'back_about.html'},'about'),
    # Examples:
    # url(r'^$', 'BBMS.views.home', name='home'),
    # url(r'^BBMS/', include('BBMS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
