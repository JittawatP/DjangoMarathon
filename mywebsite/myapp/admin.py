from django.contrib import admin
from .models import Product,Staff,ContactUs


class AllProduct(admin.ModelAdmin):
    list_display  = ('name','description','price','image','created','updated')
admin.site.register(Product,AllProduct)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'email')
admin.site.register(Staff,StaffAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'detail', 'email', 'done', 'summary')
admin.site.register(ContactUs,ContactAdmin)
