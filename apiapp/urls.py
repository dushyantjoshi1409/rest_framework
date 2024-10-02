from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/', views.index),
    path('savefile/', views.savefile),
]

