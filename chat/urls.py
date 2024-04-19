from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('increase_payment/', views.increase_payment_count, name='increase_count'),
    # path('increase_collection/', views.increase_collection_count, name='increase_count'),
    # path('increase_alarm/', views.increase_alarm_count, name='increase_count'),
    path('increase_notification/<str:notification_type>/', views.increase_count, name='increase_notification'),
    # path('total_count/', views.total_count, name='total_count'),
]
