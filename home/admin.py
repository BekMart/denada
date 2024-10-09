from django.contrib import admin
from .models import Restaurant
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):

    list_display = ('name', 'id',)
    search_fields = ['name',]
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('about',)

# Register your models here.
