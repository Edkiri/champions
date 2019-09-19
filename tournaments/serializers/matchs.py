"""Match serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import Match

# Serializers 
from .teams import TeamModelSerializer

class MatchModelSerializer(serializers.ModelSerializer):
  """Match model serializer."""

  local = TeamModelSerializer(read_only=True)
  visit = TeamModelSerializer(read_only=True)

  class Meta:
    """Meta class."""

    model = Match
    fields = (
      'local',
      'visit',
      'goals_local',
      'goals_visit',
      'date',
    )