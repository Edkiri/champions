"""Tournaments serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from tournaments.models import Tournament

class TournamentModelSerializer(serializers.ModelSerializer):
  """Tournament model serializer."""

  class Meta:
    """Meta class."""
    
    model = Tournament
    fields = (
      'name',
      'slug_name',
      'start_date',
      'image'
    )