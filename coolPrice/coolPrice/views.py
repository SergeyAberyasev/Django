from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from smartphone.models import *

def index(request):
    content = Smartphone.objects.all()
    contents= {
        'contents': content 
    }
    return render(request=request, template_name='smartphone/index.html',context=contents)