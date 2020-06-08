from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
  name = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=15)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name # Returns name as the main field in the admin