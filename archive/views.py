from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from django.conf import settings
from .models import Record
from .forms import RecordForm

def record_list(request):
    #return HttpResponse('Records')
    records = Record.objects.all()
    return render(request, 'archive/record_list.html', {'records': records})

def record_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'archive/record_view.html', {'record': record})

def record_create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/archive')
    return render(request, 'archive/record_form.html', {'form': form, 'action': 'Create'})

def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk)
    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('/archive')
    return render(request, 'archive/record_form.html', {'form': form, 'action': 'Update'})

def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('/archive')
    return render(request, 'archive/record_confirm_delete.html', {'record': record})



