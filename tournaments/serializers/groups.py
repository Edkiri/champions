"""Tournaments groups serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import Group, TeamGroupStage

# Serializers
from tournaments.serializers.teams import TeamModelSerializer

class TeamGroupStageSerializer(serializers.ModelSerializer):
  """ Team Group Stage Stats Serializer."""

  team = serializers.StringRelatedField()

  class Meta:
    """Meta class."""

    model = TeamGroupStage
    fields = (
      'team',
      'points',
      'won',
      'lost',
      'tied',
      'goals_scored',
      'goals_received',
      'matchs_played'
    )

class GroupModelSerializer(serializers.ModelSerializer):
  """Tournament groups model serializer."""

  class Meta:
    """Meta class."""

    model = Group
    fields = (
      'phase',
      'name',
    )