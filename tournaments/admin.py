# Django
from django.contrib import admin

# Models
from tournaments.models import (
  Match,
  Group,
  Team,
  Tournament,
  Player,
  TeamGroupStage,
  TeamTournament
)

class TournamentAdmin(admin.ModelAdmin):
  
  actions = ['create_team_stats','create_group_stage_stats', 'update_team_stats']

  def create_team_stats(self, request, queryset):
    for tournament in queryset:
      for team in tournament.teams.all():
        if not TeamTournament.tournamentects.filter(tournament=tournament, team=team):
          TeamTournament.tournamentects.create(tournament=tournament, team=team)
  
  def create_group_stage_stats(self, request, queryset):
    for group in queryset:
      for team in group.teams.all():
        if not TeamGroupStage.groupects.filter(group__tournament=group.tournament, team=team, group__phase="GS"):
          TeamGroupStage.groupects.create(group=group, team=team)

  def update_team_stats(self, request, queryset):
    for match in queryset:
      if match.is_finished and not match.is_pointed:
        # Update TeamTournament stats.
        stats_local = TeamTournament.matchects.get(team=match.local,tournament=match.tournament)
        stats_visit = TeamTournament.matchects.get(team=match.visit,tournament=match.tournament)
        
        stats_local.matches_played += 1
        stats_visit.matches_played += 1

        stats_local.goals_received += match.goals_visit
        stats_visit.goals_received += match.goals_local

        stats_local.goals_scored += match.goals_local
        stats_visit.goals_scored += match.goals_visit

        if match.winning_team == match.local:
          stats_local.won += 1
          stats_visit.lost += 1
        elif match.winning_team == match.visit:
          stats_visit.won += 1
          stats_local.lost += 1
        elif match.winning_team == None:
          stats_local.tied += 1
          stats_visit.tied += 1

        if match.group.phase == 'GS':
          stats_local_group = TeamGroupStage.matchects.get(team=match.local,group=match.group)
          stats_visit_group = TeamGroupStage.matchects.get(team=match.visit,group=match.group)
          
          stats_local_group.matches_played += 1
          stats_visit_group.matches_played += 1

          stats_local_group.goals_received += match.goals_visit
          stats_visit_group.goals_received += match.goals_local

          stats_local_group.goals_scored += match.goals_local
          stats_visit_group.goals_scored += match.goals_visit

          if match.winning_team == match.local:
            stats_local_group.won += 1
            stats_local_group.points += 3
            stats_visit_group.lost += 1
          elif match.winning_team == match.visit:
            stats_visit_group.won += 1
            stats_visit_group.points += 3
            stats_local_group.lost += 1
          elif match.winning_team == None:
            stats_local_group.tied += 1
            stats_local_group.points += 1
            stats_visit_group.points += 1
            stats_visit_group.tied += 1
          stats_local_group.save()
          stats_visit_group.save()

        stats_local.save()
        stats_visit.save()
        match.is_pointed = True
        match.save()

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, TournamentAdmin)
admin.site.register(Team, TournamentAdmin)
admin.site.register(Group, TournamentAdmin)
admin.site.register(Player, TournamentAdmin)
admin.site.register(TeamGroupStage, TournamentAdmin)
admin.site.register(TeamTournament, TournamentAdmin)