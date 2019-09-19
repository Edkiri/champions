"""tournaments views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Models
from tournaments.models import Tournament

# Serializers
from tournaments.serializers import TournamentModelSerializer

class TournamentViewSet(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
  """Tournament viewset."""
  
  
  queryset = Tournament.objects.all()
  serializer_class = TournamentModelSerializer()
  lookup_field = 'slug_name'