"""Tournaments URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import tournaments as tournaments_views

router = DefaultRouter()
router.register(r'tournaments', tournaments_views.TournamentViewSet, basename='tournaments')

urlpatterns = [
  path('', include(router.urls)),
]