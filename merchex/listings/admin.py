from django.contrib import admin
from listings.models import Brand
from listings.models import Listing


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'brand', 'description', 'year', 'is_sold')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Listing, ListingAdmin)
