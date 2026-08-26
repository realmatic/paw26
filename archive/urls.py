from django.shortcuts import render

from django.urls import path
from . import views

urlpatterns = [
    path("", views.record_list),
    path('record_view/<int:id>/', views.record_view, name='record_view'),
]