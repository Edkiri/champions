"""Tournamet Groups models."""

# Django
from django.db import models

class Group(models.Model):
  """Group model."""

  tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)
  name = models.CharField(max_length=2)

  teams = models.ManyToManyField('tournaments.Team', related_name="grop_teams")

  GROUP_CHOICES = [
    ('GS', 'Group Stage'),
    ('EF', 'Eighth finals'),
    ('QF', 'Quarters Final'),
    ('SF', 'Semi Final'),
    ('TF', 'Third and Fourth'),
    ( 'F', 'Final'),
  ]
  phase = models.CharField(
    max_length=2,
    choices=GROUP_CHOICES,
    default='GS'
  )

  def __str__(self):
    """Return group name."""
    return self.phase + ' ' + self.name
    

class TeamGroupStage(models.Model):
  """Group Team stats

    This is a pivot table beetwen Group and Team in which
    handle the team stats in the group stage.
  """
  group = models.ForeignKey('tournaments.Group', on_delete=models.CASCADE)
  team = models.ForeignKey('tournaments.Team', on_delete=models.CASCADE)
  
  points = models.PositiveSmallIntegerField(default=0)
  won = models.PositiveSmallIntegerField(default=0)
  lost = models.PositiveSmallIntegerField(default=0)
  tied = models.PositiveSmallIntegerField(default=0)
  goals_scored = models.PositiveSmallIntegerField(default=0)
  goals_received = models.PositiveSmallIntegerField(default=0)
  matches_played = models.PositiveSmallIntegerField(default=0)

  def get_average_goal(self):
    return self.goals_scored - self.goals_received

  class Meta:
    ordering = ('-points',)

  def __str__(self):
    """Return team name."""
    return str(self.team) + ' for ' + str(self.group)