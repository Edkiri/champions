"""Circle serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from circles.models import Circle

# Serializers
from users.serializers import UserModelSerializer


class CircleModelSerializer(serializers.ModelSerializer):
  """Circle model serializer."""

  members = UserModelSerializer(read_only=True, many=True)

  class Meta:
    """Meta class."""

    model = Circle
    fields = (
      'name', 'slug_name',
      'about', 'picture',
      'verified', 'is_public',
      'members',
    )
    read_only_fields = (
      'is_public',
      'verified',
      'is_admin'
    )