from django.urls import path

from . import views

urlpatterns = [
    path('', views.date_today, name='index'),
]