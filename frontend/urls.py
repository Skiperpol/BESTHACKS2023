from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('sharefood/', sharefood, name='sharefood'),
    path('shareitems/', shareitems, name='shareitems'),
    path('shareskills/', shareskills, name='shareskills'),
    path('events/', events, name='events'),
    path('fundacje/', fundacje, name='fundacje'),

]