from django.contrib import admin
from .models import Time, Address, Contact, Social
from django_summernote.admin import SummernoteModelAdmin

"""
Admin configuration for the Contact Info app.
This module registers the models with Django's admin panel and customizes their
administration interface, using Summernote for rich-text fields.
"""


# Register and customize the Time model in the admin panel
@admin.register(Time)
class TimeAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Time model.
    """
    list_display = ('title', 'restaurant')
    # Enables Summernote editor for time_list field
    summernote_fields = ('time_list',)


# Register and customize the Address model in the admin panel
@admin.register(Address)
class AddressAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Address model.
    """
    list_display = ('title', 'restaurant')


# Register and customize the Contact model in the admin panel
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Contact model.
    """
    list_display = ('title', 'restaurant')


# Register and customize the Social model in the admin panel
@admin.register(Social)
class SocialAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Social model.
    """
    list_display = ('title', 'restaurant')
    # Rich-text editing enabled
    summernote_fields = ('facebook', 'instagram', 'twitter',)
