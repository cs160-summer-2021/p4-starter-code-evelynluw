# chat/urls.py
# root: /recipes/
from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipe_small_start, name="recipe_small_start"),
    path('small/', views.recipe_small, name='recipe_small'),
    path('large/', views.recipe_large, name='recipe_large'),
    path('<str:room_name>/', views.room, name='room'),

]
