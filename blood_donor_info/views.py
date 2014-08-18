# Create your views here.
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def donor_page(request):
	#template = get_template('donorinfo.html')
	#variables = Context()
	#output = template.render(variables)
	#return HttpResponse(output)
	wname=request.GET.get('name')
	return HttpResponse(wname)

def signin(request):
	state=''
	c={}
	c.update(csrf(request))
	username=password=''
	if request.POST:
		username=request.POST.get('username')
		password=request.POST.get('password')
		print username
		
		user=authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state="loggedin"
			
			else:
				state="User account inactive"
		else:
			state="Incorrect username or password"
	if state=="loggedin":
		return HttpResponseRedirect("/")
	else:
		return render_to_response("back_login1.html",{'state':state,'username':username}, RequestContext(request))

def signout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/error")


