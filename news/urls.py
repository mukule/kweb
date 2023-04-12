from django.urls import path,include
from . import views
from .views import NewsListView, NewsDetailView


app_name = 'news'
urlpatterns = [
    # path("", views.news_index, name="news_index"),
    path('', NewsListView.as_view(), name='news_index'),
    path('<int:pk>', NewsDetailView.as_view(), name='newsdetailview'),
   
  
]