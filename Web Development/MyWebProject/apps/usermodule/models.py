from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

