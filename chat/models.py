from django.db import models

class Notification(models.Model):
    TYPES = (
        ('payment', '지급결재함'),
        ('collection', '집금결재함'),
        ('alarm', '알람'),
    )
    type = models.CharField(max_length=20, choices=TYPES, verbose_name='알림 종류')
    count = models.PositiveIntegerField(default=0, verbose_name='카운트 수')
    
    class Meta:
        verbose_name = '알림'
        verbose_name_plural = '알림'
    
    def __str__(self):
        return f'카운트: {self.count}'
