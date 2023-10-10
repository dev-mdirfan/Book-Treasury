from django.db import models
from datetime import datetime

class Seller(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about = models.TextField(max_length=100, blank=True)
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    passing_year = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    is_best_seller = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
