from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeaderboardStubView.as_view(), name='leaderboard-stub'),
]