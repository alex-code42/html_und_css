from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("yes", views.yes, name="yes"),
    path("brian", views.brian, name="brian"),
    path("horst", views.horst, name="horst"),
    path("<str:names>", views.greet, name="greet")
]