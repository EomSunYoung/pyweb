from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question

# 전체 목록 조회
def index(request):
    # return HttpResponse("Welcome, My site!")
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

# 상세 페이지 조회
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/detail.html', context)

# 질문 등록
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():    # 제목을 비워놓았을 때
            question = form.save(commit=False)   # 임시 저장
            question.create_date = timezone.now()   # 등록
            question.save()    # 실제 저장
            return redirect('pybo:index')
    else:   # request.method == 'GET':
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

# 답변 등록
def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)    # 질문 1개 가져오기
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question    # 답변 1개 저장하기
            form.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'form': form}
    return render(request, 'pybo:detail', context)

