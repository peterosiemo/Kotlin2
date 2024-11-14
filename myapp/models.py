from django.db import models

# Create your models here.
class user(models.Model):
    fullname = models.CharField(max_length =50)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length =20)
    yob = models.DateTimeField()
    gender = models.CharField(max_length =10)
    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length =20)
    price = models.CharField(max_length =20)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length =50)
    email = models.EmailField()
    phone = models.CharField(max_length =20)
    datetime = models.DateTimeField()
    department = models.CharField(max_length =20)
    doctor = models.CharField(max_length =20)
    message = models.TextField()
    def __str__(self):
        return self.name
