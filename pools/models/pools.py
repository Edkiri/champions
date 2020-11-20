"""Pool Models."""

# Django
from django.db import models

class Pool(models.Model):
  """Pool model.

  Circle admin can create a pool of a tournament in which 
  members can prognosticate results to earn points."""

  circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)
  tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)

  def __str__(self):
    """Return circle and tournament of the pool."""
    return f'{str(self.tournament)} in {str(self.circle)}'