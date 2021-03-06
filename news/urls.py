from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name="news_detail"),
    path('search/', SearchListView.as_view(), name="search"),
    path('add/', NewsCreateView.as_view(), name="news_add"),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]