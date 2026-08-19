from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.conf import settings

def list(request):
    return HttpResponse('Records')

    #context = {#'records': Logview(group,user).html_list(),
    #          }
    #return render(request, 'archive/list.html', context)
