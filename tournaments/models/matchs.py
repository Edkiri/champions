"""Matchs models."""

# Django
from django.db import models

class Match(models.Model):
  """Match model."""

  tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)
  group = models.ForeignKey('tournaments.Group', on_delete=models.CASCADE)

  local = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE, related_name="local")
  visit = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE, related_name="visit")

  goals_local = models.PositiveSmallIntegerField(default=0)
  goals_visit = models.PositiveSmallIntegerField(default=0)

  start_date = models.DateTimeField()

  is_finished = models.BooleanField(default=False)

  # True when opponents are defined
  is_defined = models.BooleanField(default=False)

  @property
  def winning_team(self):
      if self.goals_local == self.goals_visit:
        return None
      elif self.goals_local > self.goals_visit:
        return self.local
      return self.visit
  
  def __str__(self):
    """Return team vs team."""

    return "{}({}) vs {}({})".format(str(self.local),self.goals_local, str(self.visit),self.goals_visit) + " at " + self.start_date.strftime("%m/%d, %H:%M")