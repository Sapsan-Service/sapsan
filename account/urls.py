from django.urls import path
from .views import *

urlpatterns = [
    path('account', index_account, name='index_account'),
]
