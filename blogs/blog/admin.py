from django.contrib import admin
from .models import Post, Category

# Post 등록
admin.site.register(Post)

# 카테고리 등록
class CategoryAdmin(admin.ModelAdmin):
    # prepopulated - 필드 이름이 동시에 기록됨
    prepopulated_fields = {'slug': ('name', )}  #튜플이나 리스트 자료구조

admin.site.register(Category, CategoryAdmin)

