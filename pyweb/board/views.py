from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from board.forms import QuestionForm, AnswerForm
from board.models import Question, Answer

from django.utils import timezone

def index(request):
    return render(request, 'board/index.html')

def question_list(request):
    # question_list = Question.objects.all();
    question_list = Question.objects.order_by('-create_date');
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)
    #return HttpResponse("test")

def detail(requset, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(requset, 'board/detail.html', context)

@login_required(login_url='common:signin') #로그인 필수(세션)
def question_create(request):
    #질문 등록
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('board:question_list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:signin')
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

# 질문 수정
@login_required(login_url='common:signin')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

# 질문 삭제
@login_required(login_url='common:signin')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:question_list')

# 답변 수정
@login_required(login_url='common:signin')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.author = request.user
            answer.save()
            return redirect('board:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'form': form}
    return render(request, 'board/answer_form.html', context)

# 답변 삭제
@login_required(login_url='common:signin')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('board:detail', question_id=answer.question.id)