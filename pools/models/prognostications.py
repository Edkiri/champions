"""Prognostication matches model."""

# Django
from django.db import models

class Prognostication(models.Model):
  """Prognostication model

  Handle the prognosticatio data from users in a pool."""

  member = models.ForeignKey('circles.Membership', on_delete=models.CASCADE)
  pool = models.ForeignKey('pools.Pool', on_delete=models.CASCADE)

  points = models.PositiveSmallIntegerField(default=0)

  def __str__(self):
    """Return user and his points"""
    return f'{str(self.member.user)} {self.points} points'

class ProgMatch(models.Model):
  """Prognostication match.

  Handle the pronostication matches that users make for earning points."""

  prognostication = models.ForeignKey(
    'pools.Prognostication', 
    on_delete=models.CASCADE
    )
  match = models.ForeignKey(
    'tournaments.Match', 
    on_delete=models.CASCADE,
    related_name="prog_match"
    )
  group = models.ForeignKey(
    'tournaments.Group', 
    on_delete=models.CASCADE
    )
  prog_local = models.ForeignKey(
    'tournaments.Team', 
    on_delete=models.CASCADE, 
    related_name="prog_local",
    default=None
    )
  prog_visit = models.ForeignKey(
    'tournaments.Team', 
    on_delete=models.CASCADE,
    related_name="prog_visit",
    default=None
    )
  goals_local = models.PositiveSmallIntegerField(default=0)
  goals_visit = models.PositiveSmallIntegerField(default=0)

  has_rated = models.BooleanField(default=False)
  points = models.PositiveSmallIntegerField(default=0)

  @property
  def winning_team(self):
    if self.goals_local == self.goals_visit:
      return None
    elif self.goals_local > self.goals_visit:
      return self.prog_local
    return self.prog_visit

  def __str__(self):
    """Return team vs team."""
    return "{}({}) vs {}({})".format(str(self.prog_local),self.goals_local, str(self.prog_visit),self.goals_visit)