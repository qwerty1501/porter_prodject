from django.db import models


class Feedback(models.Model):
    
    class Meta:
        verbose_name = 'Форма братной сяви'
        verbose_name_plural = 'Форма братной сяви'
    
    name = models.CharField(verbose_name='Ф.И.О', max_length=100)
    phone = models.CharField(verbose_name='Номер телефона', max_length=30)
    poter = models.BooleanField(verbose_name='Портер', default=False)
    movers = models.BooleanField(verbose_name='Грузчики', default=False)
    dispersal = models.BooleanField(verbose_name='Разборка/сборка мебели', default=False)
    trash = models.BooleanField(verbose_name='Вызов мусора', default=False)
    description = models.TextField('Описание', blank=True, null=True)
    
    def __str__(self):
        return self.name