from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<str:slug>/question/create/', views.cate_question_create,
         name='cate_question_create'),  # 질문 등록
    path('answer/create/<int:question_id>/', views.answer_create,
         name='answer_create'),    #답변 등록
    path('question/modify/<int:question_id>/', views.question_modify,
         name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete,
         name='question_delete'),  #질문 삭제
    path('answer/delete/<int:answer_id>/', views.answer_delete,
         name='answer_delete'),   #답변 삭제
    path('comment/create/question/<int:question_id>/', views.comment_create_question,
         name='comment_create_question'),  #질문 댓글 등록
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question,
         name='comment_delete_question'),  #질문 댓글 삭제
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question,
         name='comment_modify_question'),  #질문 댓글 수정
]