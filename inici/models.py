from __future__ import unicode_literals

from django.db import models

# Create your models here.
class inici(models.Model):
	titol_inici = models.CharField('Titol Inici',max_length=40)
	mail_inici = models.EmailField(max_length=80,blank=True)
	

	def __unicode__(self):
		return u'%s' % (self.titol_inici)

	class Meta:
		ordering = ['titol_inici']