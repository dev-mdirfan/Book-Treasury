from django.shortcuts import render
from sellers.models import Seller
from books.models import Book
from books.choices import get_publication_choices, get_published_year_choices, get_price_choices

def home(request):
    books = Book.objects.order_by('-listing_date').filter(is_published=True)[:3]
    
    context = {
        'books': books,
        'publication_choices': get_publication_choices,
        'published_year_choices': get_published_year_choices,
        'price_choices': get_price_choices,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    sellers = Seller.objects.order_by('-join_date')
    is_best_seller = Seller.objects.all().filter(is_best_seller=True)
    context = {
        'sellers': sellers,
        'is_best_seller': is_best_seller,
    }
    return render(request, 'pages/about.html', context)




