from django.conf.urls import url
from playerRegister import views

urlpatterns = [
	url(r'^$', views.registration, name='registration'),
]