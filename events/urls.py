from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from events.views import *

urlpatterns=patterns('',
	(r'^$',direct_to_template,{'template':'events.html'},'events'),
	(r'^register/$',register_event),
	(r'^successful/$',direct_to_template,{'template':'thanks.html'},'successful'),
	)
