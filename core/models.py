from django.db import models

# Create your models here.


class GannonPaul(models.Model):
	talonharrison = models.CharField(max_length=100, null=True, blank=True )
	yvonnerosales = models.CharField(max_length=80, null=True, blank=True )
	rubysaunders = models.CharField(max_length=100, null=True, blank=True )
	walkerduran = models.CharField(max_length=500, null=True, blank=True )

class Testmodel(models.Model):
	test1 = models.CharField(max_length=500, null=True, blank=True )
	test2 = models.CharField(max_length=500, null=True, blank=True )