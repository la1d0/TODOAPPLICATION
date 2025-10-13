from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Todotask(models.Model):
    class Status(models.IntegerChoices):
        NOT_DONE = 0, 'В процессе'
        DONE = 1, 'Сделано'
    title = models.CharField(max_length=255,
                             verbose_name='Название',
                             )
    content = models.TextField(blank=True,
                               verbose_name='Содержание')
    status = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                 default=Status.NOT_DONE,
                                 verbose_name="Статус",
                                 )
    time_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Время создания')
    time_edited = models.DateTimeField(auto_now=True,
                                       verbose_name='Время последнего изменения')
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='tasks',
                               null=True,
                               default=None,
                               )

    def get_absolute_url(self):
        return reverse('home')