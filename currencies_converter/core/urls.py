from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('main_page', currencies_logic, name= 'main_page'),
]