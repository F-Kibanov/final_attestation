from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.show_all_recipes, name='recipes'),
    path('recipe/<int:pk>/', views.show_recipe, name='recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_user/', views.add_user, name='add_user'),
    path('user/<int:pk>/', views.show_user, name='user'),
    path('users/', views.show_all_users, name='users'),
    path('user/<int:pk>', views.show_user, name='users'),
    path('del_user/<int:pk>/', views.del_user, name='del_user'),
    path('del_recipe/<int:pk>/', views.del_recipe, name='del_recipe'),
]
