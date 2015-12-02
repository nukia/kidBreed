from django.conf.urls import url
from playerAuth import views

urlpatterns = [
	url(r'^faq/$', views.getFAQ, name='getFAQ'),
	url(r'^contact/$', views.getContact, name='getContact'),
	url(r'^', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
]