"""Player models."""

# Django
from django.db import models

class Player(models.Model):
  """Player model."""

  first_name = models.CharField(max_length=80)
  last_name = models.CharField(max_length=80)

  goals = models.PositiveSmallIntegerField()

  team = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE)

  picture = models.ImageField(
    'player image',
    upload_to='players/images/',
    blank=True,
    null=True
  )

  def __str__(self):
    """Return player last_name."""
    return self.last_name
