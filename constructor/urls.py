from django.urls import path
from . import views

urlpatterns = [
    path('constructor/', views.constructor),
]