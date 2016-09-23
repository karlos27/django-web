from django.shortcuts import render

# Create your views here.
def dades_contacta(request):
	#consulta de les dades
	dataCont = contacta.objects.order_by('id_persona')
	#renderitzar la pagina
	return render(request,'contacta.html',{'dataCont':dataCont})