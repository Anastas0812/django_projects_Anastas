from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='measurements/images/', null=True, blank=True) #путь куда будут загружаться фотки, если нет фоток будет нулл

    def __str__(self):
        return f'Measurement for {self.sensor.name} at {self.created_at}'

