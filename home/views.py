from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.conf import settings

def index(request):
    return HttpResponse('home/index')
    context = {}
    return render(request, 'index.html', context)