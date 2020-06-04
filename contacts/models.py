from django.db import models

from datetime import datetime

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True) # Boolean set top true: field can be blank
  contact_date = models.DateTimeField(default=datetime.now, blank=True) # Set date and time as default value. datetime is imported
  user_id = models.IntegerField(blank=True)
  
  def __str__(self):
    return self.name