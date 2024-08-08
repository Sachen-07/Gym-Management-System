from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    membership = models.CharField(max_length=20)
    expiration_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name


# Create your models here.