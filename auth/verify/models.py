from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name='компания', on_delete=models.CASCADE, default=2)
    url = models.CharField(max_length=355)
    calls_remaining = models.IntegerField(verbose_name='Количество оставшихся звонков')
    balance = models.IntegerField(verbose_name='Остаток на балансе')
    coast_call = models.IntegerField(verbose_name='Стоимость звонка')
    exp = models.DateField('звонки активны до:', default=datetime.date.today()+datetime.timedelta(days=180))

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'

    def __str__(self):
        return str(self.user)


class MakeCall(models.Model):
    user = models.ForeignKey(User, verbose_name='компания', on_delete=models.CASCADE)
    call_token = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Данные запроса звонка'
        verbose_name_plural = 'Данные запроса звонков'

    def __str__(self):
        return str(self.user)


class UserCalls(models.Model):
    user = models.ForeignKey(User, verbose_name='компания', on_delete=models.CASCADE)
    out_number = models.CharField(verbose_name='исходящий номер', max_length=15)
    verify_number = models.CharField(verbose_name='проверочный номер', max_length=15)
    call_date = models.DateTimeField(verbose_name='Дата и время вызова', default=datetime.datetime.now())
    class Meta:
        verbose_name = 'История звонков'
        verbose_name_plural = 'История звонков'

    def __str__(self):
        return str(self.user)