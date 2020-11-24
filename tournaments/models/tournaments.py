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

  teams = models.ManyToManyField('tournaments.Team', related_name="teams")

  def __str__(self):
    """Return Turnament name."""
    return self.name