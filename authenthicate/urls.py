
from django.contrib.auth import login
from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.login_user, name="login"),
    path('logout/',views.logout_user, name='logout'),
    path('userRegister/', views.register_user, name='uregister'),
    path('cafeRegister/', views.register_restaurant , name='cregister'),
    
]
