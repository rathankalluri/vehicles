from django.http import HttpResponse
from dealer.models import autos
from django.shortcuts import render
import pandas as pd
from django.utils.encoding import smart_str
import os
import dealer
import django.middleware.csrf
# Create your views here.

def index(requests):
	output = autos.objects.all()
	return render(requests, 'dealer/index.html', context={'output':output},)

def test_form(requests):
	return render(requests, 'dealer/test_form.html', context={'csrf': django.middleware.csrf.get_token(request)}, )

def excelgen(requests):

	pth = os.path.join(os.path.abspath(os.path.dirname(dealer.__file__)), "../")
	df = pd.DataFrame(list(autos.objects.all().values('auto_id', 'auto_man', 'year','active','dealer_id')))
	new_index = ['auto_id', 'auto_man', 'year','active','dealer_id']
	df.reindex(new_index)
	filename = 'report.xlsx'
	writer = pd.ExcelWriter(filename)
	df.to_excel(writer, 'Sheet1')
	writer.save()

	response = HttpResponse(content_type='application/vnd.ms-excel')
	#response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
	response['X-Sendfile'] = smart_str(pth)
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
	return response


def create_new(requests):
	return HttpResponse("SuccessFromViews")

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
