from django.contrib import admin
from django.urls import path
from mahalla_app.views import HomeView
from accounts.views import RegisterView, LoginView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', RegisterView.as_view(), name='home'),
]