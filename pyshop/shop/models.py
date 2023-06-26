from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)  # 비어있어도 됨
    slug = models.SlugField(max_length=200, db_index=True,
                unique=True, allow_unicode=True) # 경로 이름 한글 -all_unicode

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'  # 모델의 복수형 이름

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # product 페이지 경로
        return reverse('shop:product_in_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                    null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)  # 상세 설명
    meta_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # 가격(소수 2째, 전체 10자리)
    stock = models.PositiveIntegerField()  # 재고
    available_display = models.BooleanField('Display', default=True) # verbose name - 'Display'
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']
        index_together = [['id', 'slug']]  # index 기준 혼합

    def __str__(self):
        return self.name

    def get_absolute_url(self): #제품 상세페이지 경로
        return reverse('shop:product_detail', args=[self.id, self.slug])

