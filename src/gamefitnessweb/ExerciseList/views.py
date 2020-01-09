
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Choice, Question
# from articles.models import article

# class ArticleDetailView(DetailView):
#     model = Article
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

class IndexView(generic.ListView):
    template_name = 'ExerciseList/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last ten published questions."""
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'ExerciseList/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'ExerciseList/detail.html'



# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'ExerciseList/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('ExerciseList:results', args=(question.id,)))
#
