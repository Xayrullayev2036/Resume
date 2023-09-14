from django.urls import path
from account import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]


