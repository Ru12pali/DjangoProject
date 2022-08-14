from django.db import models

# Create your models here.
class train(models.Model):
    train_id = models.IntegerField(primary_key=True)
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
    dept_time = models.TimeField()
    arr_time = models.TimeField()
    total_seats = models.IntegerField(default=250)
    train_name = models.CharField(max_length=50)

class user(models.Model):
    user_name = models.CharField(max_length=20,primary_key=True)
    user_password = models.CharField(max_length=10)

class train_stations(models.Model):
    train = models.ForeignKey(train, on_delete=models.CASCADE)
    station_1 =  models.CharField(max_length=50)
    station_2 =  models.CharField(max_length=50)

