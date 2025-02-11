from django.contrib import admin
from .models import Menu, Type, Food, Drink
from django_summernote.admin import SummernoteModelAdmin

"""
Admin configuration for the Menu app.
This module registers and customizes the administration interface
for the Menu, Type, Food, and Drink models using Summernote for
rich-text fields.
"""


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Menu model.
    """
    list_display = ('restaurant', 'title',)
    # Enables Summernote editor for these fields
    summernote_fields = ('about', 'note')


@admin.register(Type)
class TypeAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Type model.
    """
    list_display = ('name',)
    search_fields = ['name']  # Enables search functionality by type name
    list_filter = ('name',)  # Adds a filter by name
    # Auto-generates slug from the name
    prepopulated_fields = {'slug': ('name',)}
    # Enables Summernote editor for description field
    summernote_fields = ('description')


@admin.register(Food)
class FoodAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Food model.
    """
    list_display = ('name', 'type', 'price', 'calories',)
    search_fields = ['name', 'type__name']
    list_filter = ('type', 'vegetarian', 'vegan', 'gluten',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description')


@admin.register(Drink)
class DrinkAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Drink model.
    """
    list_display = ('name', 'type', 'price', 'calories',)
    search_fields = ['name', 'type__name']
    list_filter = ('type', 'vegetarian', 'vegan', 'gluten',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description')
