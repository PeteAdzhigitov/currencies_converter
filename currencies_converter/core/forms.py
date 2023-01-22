import json
import os

from django import forms
import requests
import ast
import json
import os

apikey = os.environ.get('API_KEY_FOR_CURRENCY')
def get_currencies():
    currencies = requests.get(f'https://api.apilayer.com/currency_data/live?apikey={apikey}')
    data = currencies.text
    proper_dict = json.loads(data)
    cur = proper_dict['quotes']
    return cur

print(get_currencies())

c = [(k[3:],k[3:]) for k,v in get_currencies().items()]

class QuantyToConvert(forms.Form):
    quantity_of_money_to_convert = forms.IntegerField(min_value=1,)
    convert_from = forms.ChoiceField(choices=c)
    convert_to = forms.ChoiceField(choices=c)


