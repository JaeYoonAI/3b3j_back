from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from alpha_critic.views import index
from alpha_critic.views import detail
from . import views

urlpatterns = [
    path('',index),
    path('details/', views.detail ,name='details'),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("contents/", include("contents.urls")),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
