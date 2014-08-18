from django.conf.urls import patterns, include, url
from donorfinder.views import *
from django.views.generic.simple import direct_to_template

urlpatterns=patterns('',
	(r'^$', direct_to_template,{'template':'web_index.html'},'index'),
	
	)
