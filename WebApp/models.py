from django.db import models

class Driver(models.Model):
    dname = models.CharField(max_length=255)

    def __str__(self):
        return self.dname

class Car(models.Model):
    cname = models.CharField(max_length=255)
    drivers = models.ManyToManyField(Driver, )

    def __str__(self):
        return self.cname