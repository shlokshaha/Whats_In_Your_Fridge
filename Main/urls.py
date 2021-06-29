from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Main-home'),
    path('instructions/', views.instructions, name='Main-instructions'),

]