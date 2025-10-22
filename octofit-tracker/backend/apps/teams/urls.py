from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, TeamActivityViewSet

router = routers.DefaultRouter()
router.register(r'', TeamViewSet, basename='team')
router.register(r'activities', TeamActivityViewSet, basename='teamactivity')

urlpatterns = [
    path('', include(router.urls)),
]