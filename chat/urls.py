from django.urls import path

from . import views

urlpatterns = [
    path('', views.selectRoom, name='selectRoom'),
    path('<str:room_name>/', views.room, name='room'),

]