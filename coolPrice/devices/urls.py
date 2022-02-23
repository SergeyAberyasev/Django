from django.urls import path
from devices.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', specifications, name='spec'),
]










