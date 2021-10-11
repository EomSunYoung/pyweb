from django.contrib import admin
from .models import Question, Answer

# model 등록
admin.site.register(Question)
admin.site.register(Answer)
