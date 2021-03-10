from django.shortcuts import render, redirect

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def index(request):
    questions = Question.objects.all()

    context = {'questions': questions}
    return render(request, 'polls/index.html', context)

def create_question(request):
    if request.method != 'POST':
        question_form = QuestionForm()
    else:
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save()
            return redirect('polls:create_answer', new_question.id)

    context = {'question_form': question_form}
    return render(request, 'polls/create_question.html', context)

def create_answer(request, q_id):
    question = Question.objects.get(id=q_id)

    if request.method != 'POST':
        answer_form = AnswerForm()
    else:
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.question = question
            new_answer.save()
            return redirect('polls:create_answer', question.id)

    context = {'answer_form': answer_form, 'question': question}
    return render(request, 'polls/create_answer.html', context)

def vote(request, q_id):
    question = Question.objects.get(id=q_id)
    answers = question.answer_set.all()

    if request.method == 'POST':
        answer = Answer.objects.get(answer_text=request.POST['vote'])
        answer.votes += 1
        answer.save()

        return redirect('polls:index')

    context = {'question': question, 'answers': answers}
    return render(request, 'polls/vote.html', context)

def results(request, q_id):
    question = Question.objects.get(id=q_id)
    answers = question.answer_set.all()

    context = {'question': question, 'answers': answers}
    return render(request, 'polls/results.html', context)