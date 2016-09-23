from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class categoria (models.Model):
	id_categoria = models.AutoField(primary_key=True)
	titol_categoria = models.CharField('Titol de la categoria',max_length=50)
	#pare_categoria= models.ForeignKey(categoria)

	def __unicode__(self):
		return u'%s' % (self.titol_categoria)

	class Meta:
		ordering = ['titol_categoria']

class post_noticia (models.Model):
	id_post_noticia = models.AutoField(primary_key=True)
	titol_post_noticia = models.CharField('Titol noticia',max_length=100)
	text_post_noticia = models.TextField('Contingut de la noticia')	
	autor_post_noticia = models.ForeignKey('auth.User')
	creacio_post_noticia = models.DateTimeField(default=timezone.now)
	#cod_categoria = models.ForeignKey(categoria)

	def __unicode__(self):
		return u'%s' % (self.titol_post_noticia)

	class Meta:
		ordering = ['titol_post_noticia']

