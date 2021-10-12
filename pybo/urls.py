from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    # 127.0.0.1:8000/pybo/
    path('', views.index, name='index'),
    # 127.0.0.1:8000/pybo/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 127.0.0.1:8000/question/create
    path('question/create/', views.question_create, name="question_create"),
]