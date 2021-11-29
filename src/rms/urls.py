from django.contrib import admin
from django.urls import path
from menu.views import food_list_view
from home.views import home
from about.views import about
from cart.views import cart
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', food_list_view, name='menu'),
    path('cart/', cart, name='cart'),
    path('admin/', admin.site.urls),
]

#ALLOWS PROCESSING OF STATIC ITEMS LOCALLY
#in production using a CDN is recommended
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)