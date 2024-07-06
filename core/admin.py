# admin.py
from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image', 'uploaded_at')
