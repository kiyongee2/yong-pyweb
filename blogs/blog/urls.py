from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
]