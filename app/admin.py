from django.contrib import admin
from .models import Product
from .models import Diet
from .models import Customer
from .models import Track

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'time', 'sets', 'description', 'category','product_image' ]




@admin.register(Diet)
class DietModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'quantity', 'description', 'type','product_image' ]


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user', 'locality', 'city', 'zipcode']



@admin.register(Track)
class TrackModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user', 'product',]
