#urls de inici
from django.conf.urls import include,url
from .import views

urlpatterns = [
	url(r'^$',views.inici),
	url(r'^inici/',views.inici),
	]