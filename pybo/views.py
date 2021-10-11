from django.http import HttpResponse
from django.shortcuts import render
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