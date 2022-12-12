from django.urls import path

from SmartGrowingCore import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('productos/', views.productos, name="Productos"),
    path('desarrollo/', views.desarrollo, name="Desarrollo"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
