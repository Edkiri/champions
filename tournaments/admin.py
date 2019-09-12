# Django
from django.contrib import admin

# Models
from tournaments.models import (
  Match,
  TournamentGroup,
  Team,
  Player,
  Tournament
)

class TournamentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, TournamentAdmin)
admin.site.register(Team, TournamentAdmin)
admin.site.register(TournamentGroup, TournamentAdmin)
admin.site.register(Player, TournamentAdmin)