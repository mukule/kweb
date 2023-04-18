from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Choice, Poll
from django.views.generic.detail import DetailView
from .forms import VoteForm
from django.contrib import messages
from django.views import View



def index(request):
    latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now(), end_date__gte=timezone.now())
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)



