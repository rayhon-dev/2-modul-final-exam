from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('success/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/update/', views.UpdateProfileView.as_view(), name='update_profile'),
]