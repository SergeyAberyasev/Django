from django.urls import path
from smartphone.views import *

urlpatterns = [
    path('', index_SP, name='index_sp'),
    path('<int:id>/', specifications, name='spec'),
]










