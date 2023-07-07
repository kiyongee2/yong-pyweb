from django.urls import path
from . import views

app_name = 'ocr'

urlpatterns = [
    path('', views.ocr_read, name='ocr_read'),
]
