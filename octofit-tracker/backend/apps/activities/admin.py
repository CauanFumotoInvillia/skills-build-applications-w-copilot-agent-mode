from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = ('_id', 'name', 'user', 'date')
    search_fields = ('name', 'user__username')
