from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.

admin.site.register(Category)
#was 'admin.site.register(Page)' before. 
admin.site.register(Page, PageAdmin) 








