from django.contrib import admin
from .models import Post, Menu, Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = 'content'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter  = ('name', 'price')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('name', 'email', 'date')

