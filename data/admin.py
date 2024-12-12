from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    list_display = ('user', 'IP', 'type', 'created_at')
admin.site.register(CustomUser,CustomAdmin)