from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Choice, Poll
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.views import View
from django.db.models import F





def index(request):
    latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now(), end_date__gte=timezone.now()).order_by(F('pub_date').asc())
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/poll_detail.html'
    context_object_name = 'poll'


def results(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    
    # Check if the user has already voted on this poll
    if f'poll_{pk}_voted' in request.session:
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'error_message': "You have already voted on this poll.",
        })
    
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        # Store the fact that the user has voted on this poll in session data
        request.session[f'poll_{pk}_voted'] = True
        
        return redirect('polls:results', pk=poll.pk)
