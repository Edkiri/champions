"""Circle views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Permissions
from rest_framework.permissions import IsAuthenticated
from circles.permissions.circles import IsCircleAdmin


# Serializers
from circles.serializers import CircleModelSerializer

# Models
from circles.models import Circle, Membership

class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
  """Circle view set."""

  serializer_class = CircleModelSerializer
  lookup_field = 'slug_name'


  def get_queryset(self):
    """Restrict list to public only."""
    queryset = Circle.objects.all()
    if self.action == 'list':
      return queryset.filter(is_public=True)
    return queryset

  def get_permissions(self):
    """Assign permissions based on action."""
    permissions = [IsAuthenticated]
    if self.action in ['update', 'partial_update']:
      permissions.append(IsCircleAdmin)
      print([permission() for permission in permissions])
    return [permission() for permission in permissions]

  def perform_create(self, serializer):
    circle = serializer.save()
    user = self.request.user
    profile = user.profile
    Membership.objects.create(
      user=user,
      profile=profile,
      circle=circle,
      is_admin=True,
      remaining_invitations=10
    )