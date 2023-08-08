from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)     # 카테고리 이름 - 중복불가
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)    # url과 연동, 중복불가, 유니코드(한글포함)가능

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('board:category_page', args=[self.slug])  # reverse 방식으로 변경

    class Meta:     # 중첩 모델
        verbose_name = 'category'
        verbose_name_plural = 'categories'  # 복수형 단어 직접 지정

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #글쓴이
    subject = models.CharField(max_length=200)  #제목
    content = models.TextField()                #질문 내용
    create_date = models.DateTimeField()        #등록일
    modify_date = models.DateTimeField(null=True, blank=True) #null 허용
    # 카테고리: FK(null/공백 가능, 삭제 비연동)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.subject

# 답변 모델(테이블)
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #글쓴이
    content = models.TextField()  #답변 내용
    create_date = models.DateTimeField()  #등록일
    modify_date = models.DateTimeField(null=True, blank=True)  # null 허용
    question = models.ForeignKey(Question,
                on_delete=models.CASCADE) #외래키

    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True,
                               on_delete=models.CASCADE)