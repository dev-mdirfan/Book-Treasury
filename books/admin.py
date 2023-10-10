from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'listing_date', 'seller')
    list_display_links = ('id', 'title')
    list_filter = ('seller', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author', 'price', 'publication', 'published_year')
    list_per_page = 25

admin.site.register(Book, BookAdmin)

