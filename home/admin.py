from django.contrib import admin
from .models import Restaurant, About, Produce, Visit
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):

    list_display = ('name', 'id',)
    search_fields = ['name',]
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('about',)

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)
    summernote_fields = ('content',)

@admin.register(Produce)
class ProduceAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)
    summernote_fields = ('content',)

@admin.register(Visit)
class VisitAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id',)
    summernote_fields = ('content',)

# Register your models here.
