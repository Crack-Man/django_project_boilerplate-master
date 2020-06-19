from django.contrib import admin

# Register your models here.
from .models import Item, OrderItem, Order, Image, New, Recording


#admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
#admin.site.register(Image)
#admin.site.register(New)


@admin.register(Item)  
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter = ('status','category')

@admin.register(Image)  
class PostAdmin(admin.ModelAdmin):  
    list_display = ('id','status')
    list_filter = ['status']

@admin.register(New)  
class PostAdmin(admin.ModelAdmin):  
    list_display = ('title','status')
    list_filter = ['status']

@admin.register(Recording)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'auth', 'call')
    search_fields = ('id', 'title')
    list_filter = ['title']