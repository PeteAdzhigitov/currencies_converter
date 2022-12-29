import csv
import requests

from django.shortcuts import render
# from currencies_converter.core.forms import QuantyToConvert

# Create your views here.

def currencies_logic(request):

    API_KEY = 'ptN804DgBqvzwVvtHPnDHwoMTSrq0lAD'
    get_data = request('https://api.exchangeratesapi.io/v1/latest?access_key=API_KEY')

    # form = QuantyToConvert(request.POST)
    with open('currencies.csv','r',encoding='UTF-8') as file:
        csvreader = csv.reader(file, delimiter='|')
        d = []
        for row in csvreader:
            d.append(row[1])

            # if request.method == 'POST':
            #     if form.is_valid():
            #         quantity_of_money = form.cleaned_data['quantity_of_money_to_convert']
            #         convert_from = form.cleaned_data['convert_from']
            #         convert_to = form.cleaned_data['convert_to']

                    # result = (quantity_of_money * convert_from) / convert_to
            # return render(request, 'core/main_page.html', {'form': form, 'csvreader': d})

            # return render(request,'core/main_page.html',{'form': QuantyToConvert()})



        # form = QuantyToConvert(request.POST)