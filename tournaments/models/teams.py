"""Team models."""

# Django
from django.db import models

class Team(models.Model):
  """Team model."""

  name = models.CharField(max_length=80)


  # Group stats
  points = models.PositiveSmallIntegerField(default=0)
  won = models.PositiveSmallIntegerField(default=0)
  lost = models.PositiveSmallIntegerField(default=0)
  tied = models.PositiveSmallIntegerField(default=0)
  goals_scored = models.PositiveSmallIntegerField(default=0)
  goals_received = models.PositiveSmallIntegerField(default=0)
  match_played = models.PositiveSmallIntegerField(default=0)
  average_goal = models.SmallIntegerField(default=0)
  position = models.PositiveSmallIntegerField(default=0)

  playing_in = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)

  def get_average_goal(self):
    return self.goals_scored - self.goals_received

  image = models.ImageField(
    'team image',
    upload_to='teams/images/',
    blank=True,
    null=True
  )

  class Meta:
    ordering = ('-points', '-average_goal')

  def __str__(self):
    """Return team name."""
    return self.name