import random

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Answer

def index(request):
    return render(request, 'main/index.html')

def questions(request):
    questions = Question.objects.order_by('-date')

    context = {
        'questions': questions,
    }

    return render(request, 'main/questions.html', context)

def ask(request):
    new_question = Question(
        text=request.POST['text'],
        author=request.POST['author'],
        color=random.choice(['blue', 'green', 'red', 'pink'])
    )
    new_question.save()

    return HttpResponseRedirect(reverse('questions'))

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    new_answer = Answer(
        text=request.POST['text'],
        question=question,
    )
    new_answer.save()

    return HttpResponseRedirect(reverse('questions'))