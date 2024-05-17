# project urls.py

from django.urls import path, include
from blog import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),  # Set login page as the homepage
    path('',views.signup, name='signup'),
    path('blog/', include('blog.urls')),  # Include blog URLs
]
