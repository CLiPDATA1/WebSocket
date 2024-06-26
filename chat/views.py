from django.shortcuts import render
from .models import Notification
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def index(request):
    payment_count = Notification.objects.filter(type='payment').first
    collection_count = Notification.objects.filter(type='collection').first
    alarm_count = Notification.objects.filter(type='alarm').first
    
    context = {
        'payment_count': payment_count,
        'collection_count': collection_count,
        'alarm_count': alarm_count,
    }
    return render(request, 'chat/index.html', context)

@require_http_methods(['POST'])
def increase_count(request, notification_type):
    notification, created = Notification.objects.get_or_create(type=notification_type)
    notification.count += 1
    notification.save()
    return JsonResponse({'카운트': notification.count})

def chatting(request):
    return render(request, 'chat/chatting.html')