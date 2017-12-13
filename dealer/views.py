from django.http import HttpResponse
from dealer.models import autos
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(requests):
	output = autos.objects.all()
	return render(requests, 'dealer/index.html', context={'output':output},)
