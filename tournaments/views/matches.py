"""Match View Set."""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

# Models
from tournaments.models import Match, Tournament

# Serializers
from tournaments.serializers import MatchModelSerializer

class MatchViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet
):
  """Tournament matches view set."""

  def dispatch(self, request, *args, **kwargs):
    """Verify that the tournament exists."""
    slug_name = kwargs['slug_name']
    self.tournament = get_object_or_404(Tournament, slug_name=slug_name)
    return super(MatchViewSet, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    """Return all matches in tournament."""
    return Match.objects.filter(
      tournament=self.tournament
    )

  def get_object(self):
    """Return the tournament match by using the pk"""
    return get_object_or_404(
    Match,
    pk=self.kwargs['pk'],
    tournament=self.tournament
  )

  def get_serializer_class(self):
    """Return serlializer class based in action."""
    return MatchModelSerializer