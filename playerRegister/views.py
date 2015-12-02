from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, loader
from playerRegister.forms import playerMainForm, playerAdditionalForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.forms.models import model_to_dict
from django.contrib import auth

def registration(request):
	args = {}
	args.update(csrf(request))
	context = RequestContext(request)
	args['playerMainForm'] = playerMainForm()
	args['playerAdditionalForm'] = playerAdditionalForm()
	if request.method == 'POST':
		print('Registration form. Request method is POST. Processing...')
		playerMF = playerMainForm(data = request.POST) #MF - Player Main Form
		playerAF = playerAdditionalForm(data = request.POST) #AF = Player Addditional Form
		print('Trying to register. Checking input data...')

		if playerMF.is_valid() and playerAF.is_valid():
			print('Data is valid.')
			playerMI = playerMF.save() #MI = Player Main Info

			playerAI = playerAF.save(commit=False) #MA = Player Additional Info
			playerAI.user = playerMI

			if 'playerProfileImage' in request.FILES:
				print('Profile picture was found. Setup user\'s picture.')
				playerAI.playerProfileImage = request.FILES['playerProfileImage']
			else:
				print ('Image was not found. Setup default profile picture.')
				playerAI.playerProfileImage = 'userMedia/profilePictures/default.jpg'

			playerAI.save()
			print('Registration success.')
			newuser = auth.authenticate(username=playerMF.cleaned_data['username'], password=playerMF.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/profile/')
		else:
			print('Invalid input data.')
			print playerMF.errors, playerAF.errors
			args['login_error'] = playerMF
	return render_to_response('registration.html', args, context)