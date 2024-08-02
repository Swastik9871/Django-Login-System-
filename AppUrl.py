from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]