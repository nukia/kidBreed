from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext, loader

# Create your views here.

def getStartPage(request):
	template = loader.get_template('index.html')
	return render_to_response('index.html', {'usernickname': auth.get_user(request).username})
