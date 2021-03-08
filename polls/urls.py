from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_question/', views.create_question, name='create_question'),
    path('create_answer/<int:q_id>', views.create_answer, name='create_answer'),
]
