"""Copa America models."""

# Django
from django.db import models

class Tournament(models.Model):
  """Tournament model"""

  name = models.CharField(max_length=80)
  slug_name = models.SlugField()
  start_date = models.DateTimeField('Start at', help_text='Date time on which the tournament starts.')
  image = models.ImageField(
    'tournament image',
    upload_to='tournamets/images/',
    blank=True,
    null=True
  )

  modified = models.DateTimeField(
    'modified at',
    auto_now=True,
    help_text='Date time on which the object was last modified.'
  )
  is_finished = models.BooleanField(default=False)

  def __str__(self):
    """Return Turnament name."""
    return self.name

class TournamentStats(models.Model):
  """Tournaments stats.

  Store util information for the end of the tournament.
  """

  best_player = models.ForeignKey('tournaments.Player', on_delete=models.CASCADE, related_name="best_player") 
  top_scorer = models.ForeignKey('tournaments.Player', on_delete=models.CASCADE, related_name="top_scorer") 
  best_goalkeeper = models.ForeignKey('tournaments.Player', on_delete=models.CASCADE, related_name="best_goalkeeper") 
