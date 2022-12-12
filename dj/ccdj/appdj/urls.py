from django.urls import path
from . import views

urlpatterns = [
    path('favfoods/', views.getfoods, name='favfoods'),
]