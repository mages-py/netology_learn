from django.db import models


def upload_path_handler(instance, filename):
    return "sensors/{id}/{file}".format(id=instance.sensor.id, file=filename)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['name']


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    img = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
        ordering = ['-created_at']
