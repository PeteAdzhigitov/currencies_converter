import csv
import requests

from django.shortcuts import render
# from currencies_converter.core.forms import QuantyToConvert

# Create your views here.

def currencies_logic(request):
    currencies = {'AUD':'48,0809',
'AZN':'41,9565',
'AMD':'18,1367',
'BYN':'26,3274',
'BGN':'38,7368',
'BRL':'13,5013',}
    # API_KEY = 'ptN804DgBqvzwVvtHPnDHwoMTSrq0lAD'
    # get_data = request('https://api.exchangeratesapi.io/v1/latest?access_key=API_KEY')

    # form = QuantyToConvert(request.POST)

    if request.method == "GET":
        with open('currencies.csv','r',encoding='UTF-8') as file:
            csvreader = csv.reader(file, delimiter='|')
            # d = []
            # for row in csvreader:
            #     d.append(row)

                # if request.method == 'POST':
                #     if form.is_valid():
                #         quantity_of_money = form.cleaned_data['quantity_of_money_to_convert']
                #         convert_from = form.cleaned_data['convert_from']
                #         convert_to = form.cleaned_data['convert_to']

                        # result = (quantity_of_money * convert_from) / convert_to
            return render(request, 'core/main_page.html', {'csvreader': currencies})
    if request.method == 'POST':
        data = request.POST
        curr_from = data.get('convert_from')
        curr_to = data.get('convert_to')
        amount_of_money = data.get('quantity_of_money_to_convert')
        converted_sum = float((amount_of_money*curr_from)/curr_to)

        return render(request,'core/main_page.html',{'converted_sum':converted_sum,'curr_from':curr_from,'curr_to':curr_to, 'amount_of_money':amount_of_money })



        # form = QuantyToConvert(request.POST)