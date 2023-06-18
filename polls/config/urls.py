from django.contrib import admin
from django.urls import path, include

from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('poll/', include('poll.urls')),
    path('ocr/', include('ocr.urls')),
]
