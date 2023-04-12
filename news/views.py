from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def news_index(request):
#     return render(request, 'news/news_index.html')

class NewsListView(ListView):
    model = News
    template_name = 'news/news_index.html'
    context_object_name = 'news'
    ordering = ['-date_posted']

class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_detail.html'