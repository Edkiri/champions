"""Champions urls."""

# Django
from django.urls import path

# Views
from tournaments.views import HomeView, TournamentDetailView


urlpatterns = [
  path('home/', HomeView.as_view(), name="home"),
  path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail')
]