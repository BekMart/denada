from django.contrib import admin
from .models import OpeningTime, Address, Contact, Social
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(OpeningTime)
class OpeningTimeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)
    summernote_fields = ('time_list',)

@admin.register(Address)
class AddressAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)

@admin.register(Social)
class SocialAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)
    summernote_fields = ('app',)