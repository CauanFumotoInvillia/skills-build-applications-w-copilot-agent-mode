from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/activities/', include('apps.activities.urls')),
    path('api/teams/', include('apps.teams.urls')),
    path('api/leaderboard/', include('apps.leaderboard.urls')),
]