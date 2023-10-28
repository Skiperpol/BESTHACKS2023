from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('sharefood/', sharefood, name='sharefood'),
    path('shareitems/', shareitems, name='shareitems'),
    path('shareskills/', shareskills, name='shareskills'),
    path('events/', events, name='events'),
    path('fundacje/', fundacje, name='fundacje'),
    path('account/', account, name='account'),
    path('login/', web_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('organizacja_form/', organizacja_form, name='organizacja_form'),
    path('food_update/<foodId>', food_update, name='food_update'),



    path('createUser', createUser, name='createUser'),
    path('AjaxCreateFood', AjaxCreateFood, name='AjaxCreateFood'),
    path('AjaxCreateItem', AjaxCreateItem, name='AjaxCreateItem'),
    path('AjaxCreateSkill', AjaxCreateSkill, name='AjaxCreateSkill'),
    path('AjaxCreateOrganization', AjaxCreateOrganization, name='AjaxCreateOrganization'),
    path('AjaxUpdateFood', AjaxUpdateFood, name='AjaxUpdateFood'),
    
]