from django.urls import path

from backend import views

urlpatterns = [
    path("api/data/", views.data)
]
