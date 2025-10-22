
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import os



def api_root(request):
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f'https://{codespace}-8000.app.github.dev'
    else:
        # fall back to request host
        base = f'{request.scheme}://{request.get_host()}'

    return JsonResponse({
        'users': f"{base}/api/users/",
        'activities': f"{base}/api/activities/",
        'teams': f"{base}/api/teams/",
        'leaderboard': f"{base}/api/leaderboard/",
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/activities/', include('apps.activities.urls')),
    # alias workouts to activities for frontend compatibility
    path('api/workouts/', include('apps.activities.urls')),
    path('api/teams/', include('apps.teams.urls')),
    path('api/leaderboard/', include('apps.leaderboard.urls')),
]