# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from events.models import *


def register_event(request):
	
	errors = []
	if request.method == 'POST':
		
		if not request.POST.get('name',''):
			errors.append('Enter the name of the Organization.')

		if not request.POST.get('location',''):
			errrors.append('Enter the location')

		if not request.POST.get('date',''):
			errors.append('Enter a valid date')

		if not request.POST.get('contact_name',''):
			errors.append('Enter contact person name')

		if not request.POST.get('contact',''):
			errors.append('Enter a valid contact number')

		if not request.POST.get('email',''):
			errors.append('Enter a valid email')
		
		if not request.POST.get('no_of_donors',''):
			errors.append('Enter the expected number of donors')
		
		if not request.POST.get('details',''):
			errors.append('Enter the details')

		if not errors:
			event_object = Event(
			organization_name=request.POST.get('name'),
			where=request.POST.get('location'),
			when=request.POST.get('date'),
			contact_person_name=request.POST.get('contact_name'),
			contact=request.POST.get('contact'),
			email=request.POST.get('email'),
			expected_no_of_donors=request.POST.get('no_of_donors'),
			event_details=request.POST.get('details'))
			event_object.save()
			return HttpResponseRedirect('/events/successful/')
		
		return render_to_response('events.html',{
		'errors':errors,
		'name':request.POST.get('name',''),
		'location':request.POST.get('location',''),
		'date':request.POST.get('date',''),
		'contact_name':request.POST.get('contact_name',''),
		'contact':request.POST.get('contact',''),
		'email':request.POST.get('email',''),
		'no_of_donors':request.POST.get('no_of_donors',''),
		'details':request.POST.get('details',''),
		},context_instance=RequestContext(request))
	else:
		c={}
		c.update(csrf(request))
		return render_to_response('events.html',c) 
	
		
	

			

	
