"""Copa America models."""

# Django
from django.db import models

class Tournament(models.Model):
  """Champion base model 
  
  Tournamet acts as an abstract base class from which every
  other tournament in the project will inherit.
  """

  name = models.CharField(max_length=80)
  slug_name = models.SlugField()
  start_date = models.DateTimeField('Start at', help_text='Date time on which the tournamet starts.')
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

  def __str__(self):
    """Return Turnamet name."""
    return self.name


