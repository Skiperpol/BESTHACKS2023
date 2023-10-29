from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path('item_update/<itemId>', item_update, name='item_update'),
    path('skill_update/<skillId>', skill_update, name='skill_update'),
    path('check_food/<foodId>', check_food, name='check_food'),
    path('check_skill/<skillId>', check_skill, name='check_skill'),
    path('check_item/<itemId>', check_item, name='check_item'),



    path('createUser', createUser, name='createUser'),
    path('AjaxCreateFood', AjaxCreateFood, name='AjaxCreateFood'),
    path('AjaxCreateItem', AjaxCreateItem, name='AjaxCreateItem'),
    path('AjaxCreateSkill', AjaxCreateSkill, name='AjaxCreateSkill'),
    path('AjaxCreateOrganization', AjaxCreateOrganization, name='AjaxCreateOrganization'),
    path('AjaxUpdateFood', AjaxUpdateFood, name='AjaxUpdateFood'),
    path('AjaxUpdateItem', AjaxUpdateItem, name='AjaxUpdateItem'),
    path('AjaxUpdateFood', AjaxUpdateFood, name='AjaxUpdateFood'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)