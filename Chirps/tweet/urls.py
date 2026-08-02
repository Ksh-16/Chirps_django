
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.tweet, name='tweet_list'),
    path('create/', views.create, name='tweet_create'),
    path('<int:tweet_id>/delete/', views.delete, name='tweet_delete'),
    path('<int:tweet_id>/edit/', views.edit, name='tweet_edit'),
] 
