# blog urls.py

from django.urls import path
from .views import home, signup, user_login, post_list, post_detail

urlpatterns = [
    path('home/', home, name='home'),  # Define home URL
    path('posts/', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
