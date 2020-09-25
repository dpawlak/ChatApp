from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from chat import views



urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
