from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.conf import settings

def index(request):
    return redirect('/archive')
    #if request.user.is_authenticated:
    #  return HttpResponse('home/index')
    #else:
    #  return redirect('/support')