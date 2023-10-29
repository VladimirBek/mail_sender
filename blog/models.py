from django.db import models

from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class BlogPost(models.Model):
    """
    Блог модель
    """
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст контента')
    image = models.ImageField(upload_to='blog_images/', verbose_name='Изображение', **NULLABLE)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    pub_date = models.DateField(default=timezone.now, verbose_name='Дата публикации')
    is_active = models.BooleanField(default=False, verbose_name='активно')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Автор')
    def __str__(self):
        return self.title

