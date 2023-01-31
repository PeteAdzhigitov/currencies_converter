from django.test import TestCase

# Create your tests here.
from requests import request

class Test:
    # def testitng_purposes(self):
    #
    #     get_data = request('https://api.exchangeratesapi.io/v1/latest?access_key=API_KEY')

    def testing_that_true_is_true(self):
        assert True == True

    def testing_sum_of_two_numbers(self):
        a = 1
        b = 2
        result = a + b
        assert result == 3
