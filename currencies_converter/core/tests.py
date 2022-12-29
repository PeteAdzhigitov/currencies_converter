from django.test import TestCase

# Create your tests here.
from requests import request

class Test:
    def testitng_purposes(self):

        get_data = request('https://api.exchangeratesapi.io/v1/latest?access_key=API_KEY')