from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),   # 127.0.0.1:8000/pybo/
    path('<int:question_id>/', views.detail, name='detail'),    # 127.0.0.1:8000/pybo/1
]