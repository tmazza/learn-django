from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'questions'

  def get_queryset(seld):
    return Question.objects.order_by('-pub_data')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

def vote(request, question_id):
  q = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = q.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': q,
      'error_message': "selecion certo",
    })
  else:
    selected_choice.votes = F('votes') +1
    selected_choice.save()    

    return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))