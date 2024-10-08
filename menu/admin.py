from django.contrib import admin
from .models import Type, Food, Drink
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Type)
class TypeAdmin(SummernoteModelAdmin):

    list_display = ('name',)
    search_fields = ['name',]
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

@admin.register(Food)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('name', 'type', 'price', 'calories',)
    search_fields = ['name', 'type',]
    list_filter = ('name', 'type', 'vegetarian', 'vegan', 'gluten',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

@admin.register(Drink)
class DrinkAdmin(SummernoteModelAdmin):

    list_display = ('name', 'type', 'price', 'calories',)
    search_fields = ['name', 'type',]
    list_filter = ('name', 'type', 'vegetarian', 'vegan', 'gluten',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

# Register your models here.
