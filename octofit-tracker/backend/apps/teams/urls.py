from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeamListView.as_view(), name='team-list'),
    path('create/', views.TeamCreateView.as_view(), name='team-create'),
    path('<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('<int:pk>/update/', views.TeamUpdateView.as_view(), name='team-update'),
    path('<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team-delete'),
]