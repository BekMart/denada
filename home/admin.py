from django.contrib import admin
from .models import Restaurant, About, Produce, Visit
from django_summernote.admin import SummernoteModelAdmin

"""
Admin configuration for the Home app.
This module registers and customizes the administration interface
for the Restaurant, About, Produce, and Visit models
using Summernote for rich-text fields.
"""


@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Restaurant model.
    """
    list_display = ('name', 'id',)
    search_fields = ['name',]
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('address', 'phone', 'email')


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for the About model.
    """
    list_display = ('restaurant', 'title',)
    # Enables Summernote editor for the content field
    summernote_fields = ('content')


@admin.register(Produce)
class ProduceAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Produce model.
    """
    list_display = ('restaurant', 'title',)
    # Enables Summernote editor for the content field
    summernote_fields = ('content')


@admin.register(Visit)
class VisitAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Visit model.
    """
    list_display = ('restaurant', 'title',)
    # Enables Summernote editor for the content field
    summernote_fields = ('content')
