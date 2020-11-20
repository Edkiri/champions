# Django
from django.contrib import admin

# Models
from tournaments.models import (
  Match,
  Group,
  Team,
  Tournament,
  Player,
  TeamGroupStage
)

class TournamentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, TournamentAdmin)
admin.site.register(Team, TournamentAdmin)
admin.site.register(Group, TournamentAdmin)
admin.site.register(Player, TournamentAdmin)
admin.site.register(TeamGroupStage, TournamentAdmin)