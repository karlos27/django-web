from django.shortcuts import render
from .models import post_noticia

# Create your views here.

def post_list(request):
	noticies = post_noticia.objects.order_by('id_post_noticia')
	return render(request,'post_list.html',{'noticies':noticies})