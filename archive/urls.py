from django.shortcuts import render

from django.urls import path
from . import views

urlpatterns = [
    path("", views.record_list),
    path('record_view/<int:pk>/', views.record_view, name='record_view'),
    path('record_new/', views.record_create, name='record_create'),
    path('record_edit/<int:pk>/', views.record_update, name='record_update'),
    path('record_delete/<int:pk>/', views.record_delete, name='record_delete'),
]