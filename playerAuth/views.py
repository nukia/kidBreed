from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.template import RequestContext, loader
from django.contrib import auth
from django.core.context_processors import csrf


def getFAQ(request):
	template = loader.get_template('faq.html')
	return render_to_response('faq.html', {'usernickname': auth.get_user(request).username})

def getContact(request):
	template = loader.get_template('contact.html')
	return render_to_response('contact.html', {'usernickname': auth.get_user(request).username})


def login(request):
	loginFailed = False
	args = {}
	args.update(csrf(request))
	if request.POST:
		print('Login form. Request method is POST. Processing...')
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		print('Trying to login like: ', username, '. Checking input data...')
		if user is not None:
			if user.is_active:
				print('User is valid.')
				auth.login(request, user)
			else:
				print('User is valid, but his account is not active.')
				return HttpResponseForbidden(content='Your account is not active.')
		else:
			loginFailed = True
			print('User is not found. Login error.')
			args['login_error'] = 'User is not found'
			return render_to_response('login.html', args)
	if request.user.is_authenticated():
		print('Login success.')
		status = 200
		return redirect ('/profile/')
	else:
		print('Request method is GET. Showing standart register form.')
		status = 401
	response = render_to_response('login.html', args, context_instance=RequestContext(request))
	response.status_code = status

	if loginFailed:
		args['authResponse'] = 'Login Failed'
	return response

def logout(request): #Check for additional variables like isLoggingOutFailed and others.
	auth.logout(request)
	print('Logout success.')
	return redirect ('/')