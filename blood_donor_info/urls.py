from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from blood_donor_info.views import *

urlpatterns=patterns('',
	(r'^add$',direct_to_template,{'template':'donorinfo.html'},'donorinfo'),
	(r'^authenticate/$',donor_page),
	)
