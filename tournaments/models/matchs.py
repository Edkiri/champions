"""Matchs models."""

# Django
from django.db import models


class Match(models.Model):
  """Match model."""

  local = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE, related_name="locals")

  visit = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE, related_name="visits")

  goals_local = models.PositiveSmallIntegerField(default=0)
  goals_visit = models.PositiveSmallIntegerField(default=0)

  date = models.DateTimeField()

  WINNERS = (
    ('L', 'Local'),
    ('V', 'Visit'),
  )
  winners = models.CharField(max_length=1, choices=WINNERS)
  @property
  def winning_team(self):
      return self.local if self.winners == 'L' else self.visit
  

  def __str__(self):
    """Return team vs team."""

    return "{}({}) vs {}({})".format(str(self.local),self.goals_local, str(self.visit),self.goals_visit) + " at " + self.date.strftime("%m/%d, %H:%M")