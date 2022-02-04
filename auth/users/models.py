from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import datetime


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class verify_number(models.Model):
    user = models.ForeignKey(User, verbose_name='компания', on_delete=models.CASCADE, default=2)
    url = models.CharField(max_length=355)
    calls_remaining = models.IntegerField(verbose_name='Количество оставшихся звонков')
    exp = models.DateField('звонки активны до:', default=datetime.date.today()+datetime.timedelta(days=180))

    class Meta:
        verbose_name = 'Данные о звонках'
        verbose_name_plural = 'Данные о звоноках'

    def __str__(self):
        return str(self.user)