from django.contrib import admin
from .models import User, Profile


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'email', 'team')
	search_fields = ('username', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'bio')
