from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increase_notification/<str:notification_type>/', views.increase_count, name='increase_notification'),
    path('chatting/', views.chatting, name='chatting'),
]
