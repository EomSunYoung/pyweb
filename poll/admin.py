from django.contrib import admin
from .models import Question, Choice

# 클래스 테이블(객체) 등록
admin.site.register(Question)
admin.site.register(Choice)
