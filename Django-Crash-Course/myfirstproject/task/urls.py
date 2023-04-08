from django.urls import path

from . import views

app_name = "task"
urlpatterns = [
    path('', views.index, name='index'),
    path("add", views.add, name='add'),
    path("yes", views.yes, name="yes"),
    path("brian", views.brian, name="brian"),
    path("horst", views.horst, name="horst"),
    path("<str:names>", views.greet, name="greet")
]