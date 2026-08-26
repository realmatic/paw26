from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.conf import settings
from .models import Record

def record_list(request):
    #return HttpResponse('Records')
    records = Record.objects.all()
    return render(request, 'archive/record_list.html', {'records': records})

def record_view(request, id):
    record = Record.objects.get(id=id)
    return render(request, 'archive/record_view.html', {'record': record})


