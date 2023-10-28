from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('sharefood/', sharefood, name='sharefood'),
    path('shareitems/', shareitems, name='shareitems'),
    path('shareskills/', shareskills, name='shareskills'),
    path('events/', events, name='events'),
    path('fundacje/', fundacje, name='fundacje'),
    path('login/', web_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]