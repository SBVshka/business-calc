from .views import *

from django.urls import path

urlpatterns = [
    path('', index),
    path('about/', about),
    path('lk/', lk),
    path('history/', history),
    path('history/<int:report_id>/', historyy)
]