from django.urls import path, include
from .views import home, login, register

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('users/', include('users.urls')),
]