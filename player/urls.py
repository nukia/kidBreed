from django.conf.urls import url
from player import views

urlpatterns = [
	#url(r'^$', views.getProfiles), #get profiles. .../profiles/ profiles.html, WSGIRequest: GET '/profiles/
	url(r'^$', views.getProfile),
    url(r'^(?P<id>[0-9]+)/$', views.getProfileInfo), # .../profiles/1/ packs.html
    #url(r'^([A-Za-z]+)/(?P<levelNameField>[A-Za-z]+)/$', views.getGameName), #.../games/logic/<name>.game
]