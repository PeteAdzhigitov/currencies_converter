import csv
import requests

from django.shortcuts import render
from .forms import QuantyToConvert

# Create your views here.



def currencies_logic(request):
    currencies = {
        'AUD':48,
        'AZN':41,
        'AMD':18,
        'BYN':26,
        'BGN':38,
        'BRL':13,}
    # API_KEY = 'ptN804DgBqvzwVvtHPnDHwoMTSrq0lAD'
    # get_data = request('https://api.exchangeratesapi.io/v1/latest?access_key=API_KEY')

    # form = QuantyToConvert(request.POST)

    if request.method == "GET":
        form = QuantyToConvert()
        # with open('currencies.csv','r',encoding='UTF-8') as file:
        #     csvreader = csv.reader(file, delimiter='|')
            # d = []
            # for row in csvreader:
            #     d.append(row)

                # if request.method == 'POST':
                #     if form.is_valid():
                #         quantity_of_money = form.cleaned_data['quantity_of_money_to_convert']
                #         convert_from = form.cleaned_data['convert_from']
                #         convert_to = form.cleaned_data['convert_to']

                        # result = (quantity_of_money * convert_from) / convert_to
        return render(request, 'core/main_page.html', {'form':form,'csvreader':currencies})
    if request.method == 'POST':
        form = QuantyToConvert(request.POST)
        if form.is_valid():
            curr_from = form.cleaned_data.get('convert_from')
            curr_to = form.cleaned_data.get('convert_to')
            amount_of_money = form.cleaned_data.get('quantity_of_money_to_convert')
            converted_sum = round((currencies[curr_from]/(currencies[curr_to]))*float(amount_of_money),2)
            # converted_sum = curr_to
            return render(request,'core/main_page.html',{'converted_sum':converted_sum,'form':form})

        return render(request,{'form':form})



        # form = QuantyToConvert(request.POST)