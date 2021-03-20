from django.urls import path

from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('discover/', discover, name='discover'),
    path('join/', join, name='join')
]

