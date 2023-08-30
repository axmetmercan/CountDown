from django.urls import path

from .views import OnProggress

urlpatterns = [
    path("", OnProggress.as_view(), name="on-progress"),
]