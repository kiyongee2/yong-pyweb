from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() # 회원 가입 저장
            #가입후 자동 로그인
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)
