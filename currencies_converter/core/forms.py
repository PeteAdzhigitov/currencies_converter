from django import forms

currencies = {
'AUD':48,
'AZN':41,
'AMD':18,
'BYN':26,
'BGN':38,
'BRL':13,}

c = [(k,k) for k,v in currencies.items()]

class QuantyToConvert(forms.Form):
    quantity_of_money_to_convert = forms.IntegerField(min_value=1,)
    convert_from = forms.ChoiceField(choices=c)
    convert_to = forms.ChoiceField(choices=c)


