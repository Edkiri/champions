"""Tournaments URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import matches as matches_views
from .views import tournaments as tournaments_views

router = DefaultRouter()
router.register(r'tournaments', tournaments_views.TournamentViewSet, basename='tournaments')
router.register(
  r'tournaments/(?P<slug_name>[-a-zA-Z0-0_]+)/matches',
  matches_views.MatchViewSet,
  basename='match'
)

urlpatterns = [
  path('', include(router.urls)),
]