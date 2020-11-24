"""tournaments views."""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Models
from tournaments.models import Tournament, Match, Group, TeamGroupStage

# Serializers
from tournaments.serializers import (
  TournamentModelSerializer,
  MatchModelSerializer,
  GroupModelSerializer,
  TeamGroupStageSerializer
)

class TournamentViewSet(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
  """Tournament viewset."""
  
  
  queryset = Tournament.objects.all()
  serializer_class = TournamentModelSerializer
  lookup_field = 'slug_name'

  def dispatch(self, request, *args, **kwargs):
    """Verify that the tournament exists."""
    slug_name = kwargs['slug_name']
    self.tournament = get_object_or_404(Tournament, slug_name=slug_name)
    return super(TournamentViewSet, self).dispatch(request, *args, **kwargs)

  @action(detail=True, methods=['get'])
  def groups(self, request, *args, **kwargs):
    groups = Group.objects.filter(tournament=self.tournament, phase='GS')
    data = {}
    for group in groups:
      stats = TeamGroupStage.objects.filter(group=group)
      data[str(group)] = TeamGroupStageSerializer(stats, many=True).data
    return Response(data)

  @action(detail=True, methods=['get'])
  def finals(self, request, *args, **kwargs):
    groups = Group.objects.filter(tournament=self.tournament).exclude(phase='GS')
    data = {}
    for group in groups:
      matches = Match.objects.filter(group=group)
      data[str(group)] = MatchModelSerializer(matches, many=True).data
    return Response(data)