from django.db import models

# Create your models here.
class Course(models.Model):
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    name = models.CharField(max_length=50)