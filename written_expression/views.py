from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .models import WrittenExpressionQuestions


def change_last_parameter(url : str, new_par) -> str:
    listed_url = url.split('/')
    base_url = '/'.join(listed_url[:-1])
    return base_url + '/' + str(new_par)


def select_quantity(request):
    """Selects the quantity of questions"""
    if request.method == 'GET':
        error = request.session.get('error', False)
        if error:
            del request.session['error']
        ctx = {
            'maximum': WrittenExpressionQuestions.objects.count(),
            'error': error
            }
        return render(request, 'written_expression/quantity.html', ctx)
    
    elif request.method == 'POST':
        # Gets number from form
        quantity = request.POST.get('quantity')
        
        if not int(quantity): # if quantity == 0:
            request.session['error'] = "Choose 1 or more questions"
            # Redirect to the same page (with an error message)
            return redirect(request.path)
        return redirect(reverse_lazy('written_expression:questions', kwargs={'quantity':quantity}))


class QuestionView(View):
    model = WrittenExpressionQuestions
    template_name = 'written_expression/questions.html'

    def get(self, request, quantity):
        self.quantity = quantity
        count = self.model.objects.count()

        if quantity > count:
            return redirect(change_last_parameter(request.path, count))

        queryset = {'list': self.get_queryset(), 'quantity': quantity}
        return render(request, self.template_name, queryset)

    def post(self, request, quantity):
        request.session['post'] = request.POST
        return redirect('written_expression:check')

    def get_queryset(self):
        """
        Gets the quantity of questions specified by the url
        """
        objs = self.model.objects
        queryset = objs.all().order_by('?')[:self.quantity]
        return queryset


class CheckAnswers(View):
    model = WrittenExpressionQuestions

    def get(self, request):
        post = request.session.get('post')
        
        if not post:
            return redirect('written_expression:quantity')

        queryset = []
        cor_incor = []

        quantity = int(post['quantity'])

        for k, v in request.session['post'].items():
            try:
                k = int(k)
            except:
                continue
            
            if k == 500:
                k = int(round(float(v), 0))
                question_time = k / quantity
                time_msg = f'You took {question_time} seconds to answer each question, '
                
                if question_time > 30:
                    time_msg += 'try to answer a bit faster'
                else:
                    time_msg += "keep going like that!"
                continue

            question = self.model.objects.get(pk = k)
            queryset += [question]
            corans = question.answers.correct.answer
            if corans == v:
                # Correct answer
                cor_incor += [True]
            else:
                # Incorrect answer
                selected_answer = self.get_answer(question.answers, v)
                correct_answer = self.get_answer(question.answers, corans)
                cor_incor.append([selected_answer, correct_answer])

        ctx= {
            'Qa': zip(queryset, cor_incor),
            'time_msg': time_msg
        }
        return render(request, 'written_expression/checkAnswers.html', ctx)
        
    def get_answer(self, obj, correct_letter):
        ans = f'({correct_letter}) '
        return ans + getattr(obj, correct_letter)