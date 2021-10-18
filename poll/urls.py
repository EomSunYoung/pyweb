from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    # poll/
    path('poll_list/', views.poll_list, name='poll_list'),
    # poll/<int:question_id>/
    path('<int:question_id>/', views.poll_detail, name='poll_detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result'),

]