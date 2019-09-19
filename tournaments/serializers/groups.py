"""Tournaments groups serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import TournamentGroup

# Serializers
from .matchs import MatchModelSerializer

class TournamentGroupModelSerializer(serializers.ModelSerializer):
  """Tournament groups model serializer."""

  matchs = MatchModelSerializer(many=True)

  class Meta:
    """Meta class."""

    model = TournamentGroup
    fields = (
      'name',
      'phase',
      'matchs'
    )