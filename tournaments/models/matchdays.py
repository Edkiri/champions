"""Matchdays models."""

# Django
from django.db import models

class Matchday(models.Model):
  """Matchday model."""

  number = models.PositiveSmallIntegerField(default=0)
  
  matchs = models.ManyToManyField('tournaments.Match')

  date = models.DateTimeField()

  def __str__(self):
    """Return matchday number."""
    return str(self.number) + " - " + self.date.strftime("%m/%d/%Y")