from django import forms



class QuantyToConvert(forms.Form):
    quantity_of_money_to_convert = forms.IntegerField(min_value=1)
    convert_from = forms.ChoiceField()
    convert_to = forms.ChoiceField()

