from django.urls import path,include
from rest_framework import routers
from . import views

urlpatterns=[
    path('register/',views.register),
    path('login/',views.login),
    path('complaint/',views.complaints),
    path('admin/',views.admin),
    path('admin/<int:id>/',views.admin)
]