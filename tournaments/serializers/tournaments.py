"""Tournaments serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import Tournament

# Serializers
from tournaments.serializers.teams import TeamModelSerializer

class TournamentModelSerializer(serializers.ModelSerializer):
  """Tournament model serializer."""

  teams = TeamModelSerializer(many=True, read_only=True)

  class Meta:
    """Meta class."""
    
    model = Tournament
    fields = (
      'name',
      'slug_name',
      'start_date',
      'image',
      'teams'
    )