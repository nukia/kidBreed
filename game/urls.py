from django.conf.urls import url
from game import views

urlpatterns = [
 url(r'^$', views.getStartPage),
 #url(r'^play/', include('game.urls')),
]