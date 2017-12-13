from django.http import HttpResponse
from dealer.models import autos
from django.shortcuts import render
import pandas as pd

# Create your views here.

def index(requests):
	output = autos.objects.all()
	return render(requests, 'dealer/index.html', context={'output':output},)

def excelgen(requests):
	import StringIO

	output = StringIO.StringIO()

	df = pd.DataFrame(list(autos.objects.all().values('auto_id', 'auto_man', 'year','active','dealer_id')))
	new_index = ['auto_id', 'auto_man', 'year','active','dealer_id']
	df.reindex(new_index)

	writer = pd.ExcelWriter('output.xlsx')
	df.to_excel(writer, 'Sheet1')
	writer.save()
	excelbook = output.getvalue()
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
	response.write(excelbook)
	return response
