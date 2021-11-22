from django.contrib import admin
from django.urls import path
from menu.views import food_list_view
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='menu/', permanent=True)),
    path('admin/', admin.site.urls),
    path('menu/', food_list_view)
]

#ALLOWS PROCESSING OF STATIC ITEMS LOCALLY
#in production using a CDN is recommended
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)