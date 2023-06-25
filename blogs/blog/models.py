from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  #카테고리 이름
    # url 주소: allow_unicode - 한글 주소
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f'/blog/category/{self.slug}'
        #reverse - 경로를 문자열로 반환(redirect와 유사)
        return reverse('blog:category_page', args=[self.slug])

    # 모델 이름이 admin에서 category -> categories로 변경됨
    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d',
                    null=True, blank=True)
    file = models.FileField(upload_to='blog/files/%Y/%m/%d',
                    null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True,
                    on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_file_name(self):
        return os.path.basename(self.file.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


