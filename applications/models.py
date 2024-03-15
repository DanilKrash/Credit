from django.contrib.auth.models import User
from django.db import models


class Credit(models.Model):
    class Purpose(models.TextChoices):
        just = 'just', 'Просто деньги'
        refinancing = 'refinancing', 'Рефинансирование кредита'
        car = 'car', 'Новая машина'
        realestate = 'realestate', 'Недвижимость'
        mortgage = 'mortgage', 'Ипотека'

    class Status(models.TextChoices):
        new = 'new', 'Новая'
        no = 'no', 'Неодобренна'
        yes = 'yes', 'Одобренна'

    price = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Сумма')
    purpose = models.CharField(choices=Purpose.choices, default=Purpose.just, max_length=15, verbose_name='Цель кредита')
    city = models.CharField(max_length=20, verbose_name='Город')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.new, verbose_name='Статус')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

