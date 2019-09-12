"""Tournamet Groups models."""

# Django
from django.db import models

class TournamentGroup(models.Model):
  """Tournamet groups model."""

  name = models.CharField(max_length=50, default="Fase de grupo")

  teams = models.ManyToManyField('tournaments.Team', related_name="teams")

  matchs = models.ManyToManyField('tournaments.Match', related_name="matchs")

  tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)

  GROUP_STAGE = 'GS'
  EIGHTH = 'EF'
  QUARTERS = 'QF'
  SEMI = 'SF'
  THIRD_AND_FOURTH = 'TF'
  FINAL = 'F'

  GROUP_CHOICES = [
    (GROUP_STAGE, 'Group Stage'),
    (EIGHTH, 'Eighth finals'),
    (QUARTERS, 'Quarters Final'),
    (SEMI, 'Semi Final'),
    (THIRD_AND_FOURTH, 'Third and Fourth'),
    (FINAL, 'Final'),
  ]
  phase = models.CharField(
    max_length=2,
    choices=GROUP_CHOICES,
    default=GROUP_STAGE
  )


  def __str__(self):
    """Return group name."""
    return self.name
