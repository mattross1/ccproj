from django.urls import path
from . import views

urlpatterns = [
    path('favfoods/', views.foodspage, name='favfoods'),
]