from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', signin, name='signin'),
    path('logout', logout, name='logout'),
]