from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop/', include('shop.urls')),  #shop
    path('cart/', include('cart.urls')),  #장바구니
    path('coupon/', include('coupon.urls')),  #쿠폰앱
    path('accounts/', include('allauth.urls')), #소셜 로그인
]

urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)