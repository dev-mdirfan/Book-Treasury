from django.contrib import admin
from .models import Seller

class SellersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_best_seller', 'passing_year', 'join_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_best_seller',)
    search_fields = ('name', 'college', 'branch', 'year', 'email')
    list_per_page = 25

admin.site.register(Seller, SellersAdmin)