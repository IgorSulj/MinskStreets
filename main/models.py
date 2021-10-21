from django.db import models


# Create your models here.

class StreetModel(models.Model):
    name = models.CharField(max_length=75, verbose_name='Имя улицы')
    slug = models.SlugField(max_length=75, verbose_name='Слаг')
    geocode = models.CharField(max_length=255, verbose_name='Геокод улицы')
    man_name = models.CharField(max_length=150, verbose_name='Имя человека')
    man_photo = models.ImageField(upload_to='people/', verbose_name='Фото человека')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class StreetPhoto(models.Model):
    street = models.ForeignKey(StreetModel, on_delete=models.CASCADE, verbose_name='Улица', related_name='photos')
    name = models.CharField(max_length=50, verbose_name='Имя фото', blank=True)
    img = models.ImageField(upload_to='streets/')
