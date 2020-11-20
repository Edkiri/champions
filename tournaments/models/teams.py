"""Team models."""

# Django
from django.db import models

class Team(models.Model):
  """Team model."""

  name = models.CharField(max_length=80)

  image = models.ImageField(
    'team image',
    upload_to='teams/images/',
    blank=True,
    null=True
  )

  def __str__(self):
    """Return team name."""
    return self.name


class TeamTournament(models.Model):
  """Tournament Team stats

    This is a pivot table beetwen Tournament and Team in which
    handle the team stats in the tournament.
  """

  tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)
  team = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE)

  # Stats
  won = models.PositiveSmallIntegerField(default=0)
  lost = models.PositiveSmallIntegerField(default=0)
  tied = models.PositiveSmallIntegerField(default=0)
  goals_scored = models.PositiveSmallIntegerField(default=0)
  goals_received = models.PositiveSmallIntegerField(default=0)
  match_played = models.PositiveSmallIntegerField(default=0)

  def __str__(self):
    """Return team name."""
    return self.team