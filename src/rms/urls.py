from django.contrib import admin
from django.urls import path
from menu.views import food_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', food_list_view)
]
