"""tournaments views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Models
from tournaments.models import Tournament, TournamentGroup

# Serializers
from tournaments.serializers import (
  TournamentModelSerializer,
  TournamentGroupModelSerializer,
)

class TournamentViewSet(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
  """Tournament viewset."""
  
  
  queryset = Tournament.objects.all()
  serializer_class = TournamentModelSerializer
  lookup_field = 'slug_name'

  def retrieve(self, request, *args, **kwargs):
    """Add extra data to the response."""
    response = super(TournamentViewSet, self).retrieve(request, *args, **kwargs)
    tournament = self.get_object()
    groups = TournamentGroup.objects.filter(
      tournament=tournament
    )
    data = {
      'tournament': response.data,
      'groups': TournamentGroupModelSerializer(groups, many=True).data
    }
    response.data = data
    return response