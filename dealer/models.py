from django.db import models

# Create your models here.

class autos(models.Model):
	auto_id = models.IntegerField()
	auto_man = models.CharField(max_length=30)
	year = models.IntegerField()
	active = models.IntegerField()
	dealer_id = models.IntegerField()