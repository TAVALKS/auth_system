from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
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


class MakeCall(models.Model):
    user = models.ForeignKey(User, verbose_name='компания', on_delete=models.CASCADE)
    call_token = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Данные о звонках'
        verbose_name_plural = 'Данные о звоноках'

    def __str__(self):
        return str(self.user)