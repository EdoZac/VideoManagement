from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice, Movie


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_movie_list'

    def get_queryset(self):
        """
        Return the last five published movies (not including those set to be
        published in the future).
        """
        return Movie.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Movie

    def get_queryset(self):
        
        return Movie.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        question = movie.question_set.get(pk=request.POST['question'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'error_message': "You didn't select a choice or question.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
