from django.contrib.auth.models import User
from player.models import playerProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class playerMainForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
class playerAdditionalForm(forms.ModelForm):
	class Meta:
		model = playerProfile
		fields = ('playerProfileImage', 'playerAge')