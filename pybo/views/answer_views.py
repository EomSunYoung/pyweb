from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question

# 답변 등록
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)    # 질문 1개 가져오기
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question    # 답변 1개 저장하기
            form.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'form': form}
    return render(request, 'pybo:detail', context)