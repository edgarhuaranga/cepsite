from django.db import models

# Create your models here.
class SensorItem(models.Model):
    sensor_id = models.CharField(max_length=200)
    sensor_value = models.FloatField()
    sensor_timestamp = models.PositiveIntegerField()
