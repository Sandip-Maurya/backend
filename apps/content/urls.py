"""
URL configuration for content app.
"""
from django.urls import path
from .views import sustainable_gifting_list_view

app_name = 'content'

urlpatterns = [
    path('sustainable-gifting/', sustainable_gifting_list_view, name='sustainable-gifting-list'),
]

