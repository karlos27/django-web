from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Dades contacte
class contacta(models.Model):
	id_persona = models.AutoField(primary_key=True)
	nom_persona = models.CharField('Nom Empresa',max_length=40)
	mail_persona = models.EmailField(max_length=80,blank=True)
	tlf_persona = models.CharField(max_length=9)
	adr_persona = models.CharField(max_length=80) 
	cp_persona = models.CharField(max_length=5)
	#logo_empresa = models.ImageField(upload_to='uploads',verbose_name='Empresa_Imatge')

	def __unicode__(self):
		return u'%s' % (self.nom_persona)

	class Meta:
		ordering = ['nom_persona']