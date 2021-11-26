from django.contrib import admin

from home.views import home
from .models import Food
# Register your models here.

admin.site.register(Food)