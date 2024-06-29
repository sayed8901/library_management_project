from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # path('logout/', views.user_logout, name='logout'),
    
    path('profile/', views.UserAccountUpdateView.as_view(), name='profile'),
    
    path('pass_change/', views.password_change, name='pass_change'),
]
