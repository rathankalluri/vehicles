from django.http import HttpResponse
from dealer.models import autos
from django.shortcuts import render
import pandas as pd
from django.utils.encoding import smart_str
import os
import dealer
# Create your views here.

def index(requests):
	output = autos.objects.all()
	return render(requests, 'dealer/index.html', context={'output':output},)

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
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
	response['X-Sendfile'] = smart_str(pth)
	return response
