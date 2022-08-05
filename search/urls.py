from .views import *
from django.urls import path

app_name = 'search'

urlpatterns = [
    path('', search, name='search'),

]