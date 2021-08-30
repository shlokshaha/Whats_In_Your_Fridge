from django.urls import path
from . import views

urlpatterns = [
    path('', views.inputPage, name='input'),
    path('veg/', views.veg, name='vegInput'),
    path('nonVeg/', views.nonVeg, name='nonVegInput'),
    path('veg_result/', views.veg_result, name='veg_result'),
    path('nonveg_result/', views.nonveg_result, name='nonveg_result'),
    path('feedback/', views.feedback, name='feedback')
]