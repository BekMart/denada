from django.contrib import admin
from .models import Menu, Type, Food, Drink
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Menu)
class TypeAdmin(SummernoteModelAdmin):

    list_display = ('restaurant', 'id',)
    summernote_fields = ('about',)

@admin.register(Type)
class TypeAdmin(SummernoteModelAdmin):

    list_display = ('name', 'id',)
    search_fields = ['name',]
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

@admin.register(Food)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('name', 'type', 'price', 'calories',)
    search_fields = ['name', 'type',]
    list_filter = ('type', 'vegetarian', 'vegan', 'gluten',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

@admin.register(Drink)
class DrinkAdmin(SummernoteModelAdmin):

    list_display = ('name', 'type', 'price', 'calories',)
    search_fields = ['name', 'type',]
    list_filter = ('type', 'vegetarian', 'vegan', 'gluten',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

# Register your models here.
