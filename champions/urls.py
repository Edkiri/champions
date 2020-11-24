"""Champions urls."""

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('tournaments.urls', 'tournaments'), namespace='tournaments')),
    path('', include(('circles.urls', 'circles'), namespace='circles')),
    path('', include(('pools.urls', 'pools'), namespace='pools')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
