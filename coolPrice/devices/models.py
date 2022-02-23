from django.urls import reverse
from django.db import models



class Smartphone(models.Model):
    data_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    url_product = models.TextField(verbose_name='URL продукта')
    url_img_prevue = models.TextField(verbose_name='IMG')
    url_imgs = models.TextField(verbose_name='IMGs')
    brand = models.CharField(max_length=10, verbose_name='Бренд')
    model = models.CharField(max_length=25, verbose_name='Модель')
    os_phone = models.CharField(max_length=10, verbose_name='OS')
    diagonal = models.FloatField(verbose_name='Диагональ экрана')
    display_type = models.CharField(max_length=10, verbose_name='Тип дисплея')
    display_height = models.IntegerField(verbose_name='Высота дисплея')
    display_width = models.IntegerField(verbose_name='Ширина дисплея')
    display_resol = models.CharField(max_length=10, verbose_name='Ширина и высота дисплея')
    ram = models.IntegerField(verbose_name='Оперативная память')
    rom = models.IntegerField(verbose_name='Объем внутренней памяти')
    camera_count = models.IntegerField(verbose_name='Количество камер')
    processor = models.CharField(max_length=30, verbose_name='Процессор')
    battery = models.IntegerField(verbose_name='Объём батареи')
    # file = models.ImageField(upload_to="img/%Y/%m/%d/", verbose_name='Путь к файлу')

    def __str__(self):
        return f"model: {self.model}"


    def get_absolute_url(self):
        return self.pk

    class Meta:
        verbose_name = 'Смартфон' # Название таблици в ед. числе
        verbose_name_plural = 'Смартфоны' # Название таблици в мн. числе
        ordering =  ['data_update'] # Сортировка статей по столбцу

# class Cat(models.Model):






