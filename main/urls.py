from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.questions, name='questions'),
    path('ask', views.ask, name='ask'),
    path('<int:question_id>/answer', views.answer, name='answer'),
]