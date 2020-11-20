"""Player Models."""

# Django
from django.db import models

class Player(models.Model):
  """Player Model."""

  name = models.CharField(max_length=80)
  team = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE)
  picture = models.ImageField(
    'player picture',
    upload_to='players/pictures/',
    blank=True,
    null=True
  )
  goals_scored = models.PositiveSmallIntegerField(default=0)