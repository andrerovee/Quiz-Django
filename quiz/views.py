from django.shortcuts import render, redirect
from .models import Question, Choice


def quiz_start(request):
    request.session['score'] = 0
    request.session['question_index'] = 0
    return redirect('quiz_question')


def quiz_question(request):
    index = request.session.get('question_index', 0)
    questions = Question.objects.all()
    if index >= len(questions):
        return redirect('quiz_result')

    question = questions[index]

    if request.method == 'POST':
        selected = request.POST.get('choice')
        if selected:
            choice = Choice.objects.get(id=selected)
            if choice.is_correct:
                request.session['score'] += 1
        request.session['question_index'] += 1
        return redirect('quiz_question')

    return render(request, 'quiz/question.html', {'question': question})


def quiz_result(request):
    score = request.session.get('score', 0)
    total = Question.objects.count()
    return render(request, 'quiz/result.html', {'score': score, 'total': total})
