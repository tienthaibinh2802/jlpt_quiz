from django.shortcuts import render, get_object_or_404
from .models import Test, Question, AnswerOption
from .forms import AnswerForm

def home(request):
    levels = ['N5', 'N4', 'N3', 'N2', 'N1']
    return render(request, 'home.html', {'levels': levels})

def test_list(request, level, category):
    tests = Test.objects.filter(level=level, category=category)
    return render(request, 'test_list.html', {
        'tests': tests,
        'level': level,
        'category': category,
    })

def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.prefetch_related('options').all()
    result = []
    score = 0

    if request.method == 'POST':
        form = AnswerForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                user_answer_id = int(form.cleaned_data.get(f"question_{question.id}"))
                correct_option = question.options.filter(is_correct=True).first()
                user_option = question.options.get(id=user_answer_id)
                is_correct = user_option.is_correct

                if is_correct:
                    score += 1

                result.append({
                    'question': question,
                    'user_option': user_option,
                    'correct_option': correct_option,
                    'is_correct': is_correct,
                })

            return render(request, 'test_result.html', {
                'test': test,
                'result': result,
                'score': score,
                'total': questions.count()
            })
    else:
        form = AnswerForm(questions=questions)

    return render(request, 'take_test.html', {
        'test': test,
        'questions': questions,
        'form': form,
    })
