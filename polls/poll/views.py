from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question, Choice


def index(request):
    return render(request, 'poll/index.html')

def poll_list(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'poll/poll_list.html', context)
    # return HttpResponse("<h2>Hello~ Django!</h2>")

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'poll/detail.html', context)

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        try:
            choice_id = request.POST['choice']
            sel_choice = question.choice_set.get(id=choice_id)
        except:
            error = "선택을 하지 않았습니다."
            return render(request, 'poll/detail.html',
                          {'question': question, 'error': error})
        else:
            sel_choice.votes = sel_choice.votes + 1
            sel_choice.save()
            return render(request, 'poll/result.html', {'question': question})
    else:
        return render(request, 'poll/detail.html', id=question_id)
