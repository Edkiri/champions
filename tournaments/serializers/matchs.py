"""Match serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import Match

class MatchModelSerializer(serializers.ModelSerializer):
  """Match model serializer."""

  local = serializers.StringRelatedField()
  visit = serializers.StringRelatedField()

  class Meta:
    """Meta class."""

    model = Match
    fields = (
      'local',
      'visit',
      'goals_local',
      'goals_visit',
      'date',
      'winners'
    )