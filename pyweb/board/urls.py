from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('answer/create/<int:question_id>/', views.answer_create,
            name='answer_create'),
    path('question/modify/<int:question_id>/', views.question_modify,
            name='question_modify'),  #질문수정
    path('question/delete/<int:question_id>/', views.question_delete,
            name='question_delete'), #질문 삭제
    path('answer/modify/<int:answer_id>/', views.answer_modify,
            name='answer_modify'), #답변 수정
    path('answer/delete/<int:answer_id>/', views.answer_delete,
            name='answer_delete'), #답변 삭제
    path('vote/question/<int:question_id>/', views.vote_question,
            name='vote_question')   #질문 추천
]