from django.db import models
from django.contrib.auth.models import User

class playerProfile(models.Model):
	user = models.OneToOneField(User)
	playerProfileImage = models.ImageField(upload_to = 'userMedia/profilePictures/', blank = True)
	playerAge = models.IntegerField(default = 6, blank = False)
	playerRating = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.user.username