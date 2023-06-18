from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from board.forms import QuestionForm, AnswerForm
from board.models import Question, Answer

from django.utils import timezone

def index(request):
    question_list = Question.objects.all();
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)
    #return HttpResponse("test")

def detail(requset, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(requset, 'board/detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    #질문 등록
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    #답변 등록
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form': form} #주의 - question 포함
    return render(request, 'board/detail.html', context)
    # question.answer_set.create(content=request.POST.get('content'),
    #                             create_date = timezone.now())