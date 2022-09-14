from django.urls import path
from django.contrib.flatpages import views
from .views import (
    NewsList, NewDetail, NewCreate, NewSearch, NewDelete, NewUpdate
)


urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewDetail.as_view()),
    path('create/', NewCreate.as_view()),
    path('search/', NewSearch.as_view(), name='news_search'),
    path('<int:pk>/delete/', NewDelete.as_view()),
    path('<int:pk>/update/', NewUpdate.as_view())
]