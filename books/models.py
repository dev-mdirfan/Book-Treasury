from django.core.validators import MinValueValidator
from django.db import models
from sellers.models import Seller
from datetime import datetime
from .year import max_value_current_year


class Book(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    publication = models.CharField(max_length=100)
    published_year = models.IntegerField(('year'), validators=[MinValueValidator(1950), max_value_current_year])
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    front_cover = models.ImageField(upload_to='covers/%Y/%m/%d/')
    back_cover = models.ImageField(upload_to='back_covers/%Y/%m/%d/')
    front_page = models.ImageField(upload_to='front_pages/%Y/%m/%d/', blank=True)
    back_page = models.ImageField(upload_to='back_pages/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    listing_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title