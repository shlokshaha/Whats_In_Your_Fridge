from django.urls import path
from . import views

urlpatterns = [
    path('', views.inputPage, name='input'),
    path('veg/', views.veg, name='vegInput'),
    path('nonVeg/', views.nonVeg, name='nonVegInput'),

]