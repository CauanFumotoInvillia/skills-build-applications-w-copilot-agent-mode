from django.urls import path
from . import views

urlpatterns = [
    # list and detail endpoints for frontend consumption
    path('', views.UserList.as_view(), name='user-list'),
    path('<str:pk>/', views.UserDetail.as_view(), name='user-detail'),

    # auth-related endpoints
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]