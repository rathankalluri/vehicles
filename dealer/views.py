from django.http import HttpResponse
from dealer.models import autos
from django.shortcuts import render
import pandas as pd
import os
import dealer
import django.middleware.csrf

# Create your views here.

def index(requests):
	output = autos.objects.all()
	return render(requests, 'dealer/index.html', context={'output':output},)

def excelgen(requests):

	df = pd.DataFrame(list(autos.objects.all().values('auto_id', 'auto_man', 'year','active','dealer_id')))
	new_index = ['auto_id', 'auto_man', 'year','active','dealer_id']
	df.reindex(new_index)

	filename = 'report.xlsx'
	writer = pd.ExcelWriter(filename)
	df.to_excel(writer, 'Sheet1')
	writer.save()

	path = os.getcwd()+'/'+filename
	file = open(path)
	response = HttpResponse(file.read(), content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename=' + filename
	response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-16'
	return response

def create_new(requests):
	if requests.method == "POST":
		create_req = autos()
		create_req.auto_id = requests.POST.get('auto_id')
		create_req.auto_man = requests.POST.get('auto_man')
		create_req.year = requests.POST.get('year')
		create_req.active = requests.POST.get('active')
		create_req.dealer_id = requests.POST.get('dealer_id')

		create_req.save()
		return HttpResponse("Created Successfully")

def update_new(requests):
	if requests.method == "POST":
		update_req = autos.objects.get(id=requests.POST.get('id'))
		update_req.auto_id = requests.POST.get('auto_id')
		update_req.auto_man = requests.POST.get('auto_man')
		update_req.year = requests.POST.get('year')
		update_req.active = requests.POST.get('active')
		update_req.dealer_id = requests.POST.get('dealer_id')

		update_req.save()
		return HttpResponse("Successfully Updated")

def delete_new(requests):
	if requests.method == "POST":
		autos.objects.filter(id=requests.POST.get('id')).delete()
		return HttpResponse("Successfully Deleted")
