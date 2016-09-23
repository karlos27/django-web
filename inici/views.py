from django.shortcuts import render
# Create your views here.
def inici(request):
	#consulta de les dades
	Inici = inici.objects.order_by('titol_inici')
	#renderitzar la pagina
	return render(request,'inici.html'),{'Inici':Inici})


