"""Match serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import Match

# Serializers
from tournaments.serializers import GroupModelSerializer

class MatchModelSerializer(serializers.ModelSerializer):
  """Match model serializer."""

  local = serializers.StringRelatedField()
  visit = serializers.StringRelatedField()

  group = GroupModelSerializer()

  class Meta:
    """Meta class."""

    model = Match
    fields = (
      'pk',
      'local',
      'visit',
      'goals_local',
      'goals_visit',
      'is_finished',
      'group'
    )