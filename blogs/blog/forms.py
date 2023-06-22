from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'file', 'category']
        labels = {
            'title': '제목',
            'content': '내용',
            'photo': '사진',
            'file': '파일',
            'category': '카테고리'
        }