from django.contrib import admin
from .models import LeaderboardEntry


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):

    list_display = ('_id', 'user', 'score', 'date')
    search_fields = ('user__username',)
