#urls de empresa
from django.conf.urls import include,url
from .import views

urlpatterns = [
	url(r'^$',views.dades_contacta),
	url(r'^contacta/',views.dades_contacta),
	]