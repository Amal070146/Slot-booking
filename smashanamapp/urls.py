from .views import signup,admin_home,login_admin,login,user_logout,admin_login,admin_logout,user_home
from django import contrib
from django.urls import include,path

urlpatterns = [
    path('',signup, name='signup'),
    path('login/',login, name='login'),
    path('login_admin/',login_admin, name='login_admin'),
    path('admin_home/',admin_home, name='admin_home'),
    path('admin_logout/',admin_logout, name='admin_logout'),
    path('user_logout/',user_logout, name='user_logout'),
    path('user_home/',user_home, name='user_home'),

]