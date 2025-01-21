
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    
] + staticfiles_urlpatterns()


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)