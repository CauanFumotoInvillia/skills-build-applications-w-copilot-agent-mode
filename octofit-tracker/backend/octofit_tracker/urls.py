
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'users': '/api/users/',
        'activities': '/api/activities/',
        'teams': '/api/teams/',
        'leaderboard': '/api/leaderboard/',
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/activities/', include('apps.activities.urls')),
    path('api/teams/', include('apps.teams.urls')),
    path('api/leaderboard/', include('apps.leaderboard.urls')),
]