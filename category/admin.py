from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoey_name',)}
    list_display = ('categoey_name','slug')

admin.site.register(Category, CategoryAdmin)

