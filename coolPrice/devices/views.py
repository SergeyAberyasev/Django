from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from devices.models import *

def index(request):
    content = Smartphone.objects.all()
    contents= {
        'contents': content
    }
    # return HttpResponse('post')
    return render(request=request, template_name='devices/index.html',context=contents)

def specifications(request, id):
    post = get_object_or_404(Smartphone, pk=id)
    # print(post) # model: GT Master Edition
    # id = int(path.split('-')[-1].replace('id', ''))
    # content = Smartphone.objects.filter(pk = id)
    # if not content:
    #     raise Http404()
    content = {
        'content': post,
        'cut_selected': post.id
    }
    return render(request, 'devices/specifications.html', content)
    # return HttpResponse(post)





def page_not_found(request, exception):
    return redirect('', permanent=True)




