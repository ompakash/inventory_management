from django.contrib import admin
from dashboard.models import *
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = "E Commerce"



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category' , 'quantity')
    list_filter = ('category',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)