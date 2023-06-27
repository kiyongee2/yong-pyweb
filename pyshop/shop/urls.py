from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_in_category, name='product_all'),
    re_path(r'^(?P<slug:category_slug>[\w]+)/$', views.product_in_category,
         name='product_in_category'),
    path('<int:id>/<slug:product_slug>/', views.product_detail,
         name='product_detail'),
]

