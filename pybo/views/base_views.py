from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question

def index(request):
    return render(request, 'pybo/index.html')

# 전체 목록 조회
def board(request):
    # 페이지 : 127.0.0.1:8000/pybo/?page=1
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    # 조회
    question_list = Question.objects.order_by('-create_date')   # 내림차순 정렬
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |    # 제목 검색
            Q(content__icontains=kw) |    # 내용 검색
            Q(answer__content__icontains=kw) |
            Q(author__username__icontains=kw) |     # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이 검색
        ).distinct()    # 중복을 제거한 유일한 내용

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}   # page와 kw 추가
    return render(request, 'pybo/question_list.html', context)

# 상세 페이지 조회
def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/detail.html', context)
