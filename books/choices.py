from .models import Book

# Get all publication choices from the database

def get_publication_choices():
    return [ publication for publication in Book.objects.all().values_list('publication', flat=True)]

# Get all publication_year choices from the database

def get_published_year_choices():
    return [publication_year for publication_year in Book.objects.all().values_list('published_year', flat=True)]

# Get all prices choices from the database

def get_price_choices():
    return [price for price in Book.objects.all().values_list('price', flat=True)]
