from django.shortcuts import render, render_to_response, redirect
from rest_framework import status
from django.http import HttpResponse
from player.models import playerProfile
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth

def getProfile(request):
	us_id = auth.get_user(request).id
	print us_id
	return getProfileInfo(request, us_id)

def getProfileInfo(request, id):
	userObject = User.objects.get(pk = id)
	playerProfileObject = playerProfile.objects.get(user_id=id)
	template = loader.get_template('profile.html')
	context = RequestContext(request, {
		'userObject': userObject, # Dictionary
		'playerProfileObject': playerProfileObject,
    })
	return HttpResponse(template.render(context))