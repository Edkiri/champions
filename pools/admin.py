# Django
from django.contrib import admin

# Models
from pools.models import ProgMatch, Pool, Prognostication

class PoolAdmin(admin.ModelAdmin):
  
  actions = ['calculte_points']

  def calculte_points(self, request, queryset):
    for obj in queryset:

      if not obj.has_rated:
        
        # +5 points if user hit the complete result.
        if (obj.prog_local == obj.match.local) and (obj.prog_visit == obj.match.visit) and \
        (obj.goals_local == obj.match.goals_local) and (obj.goals_visit == obj.match.goals_visit):
          obj.points = 5
          obj.prognostication.points = obj.prognostication.points + obj.points
          obj.prognostication.save()
          obj.has_rated = True
          obj.save()
        
        # +3 points if the user hit the winner team.
        elif (obj.winning_team == obj.match.winning_team) and (obj.winning_team):
          obj.points = 3
          obj.prognostication.points = obj.prognostication.points + obj.points
          obj.prognostication.save()
          obj.has_rated = True
          obj.save()

        # +1 points if the user hit a tie but no result.
        elif (obj.winning_team == obj.match.winning_team) and not (obj.winning_team):
          obj.points = 1
          obj.prognostication.points = obj.prognostication.points + obj.points
          obj.has_rated = True
          obj.prognostication.save()
          obj.save()
      
  calculte_points.short_description = 'Calculate prognostication points'

admin.site.register(ProgMatch, PoolAdmin)
admin.site.register(Pool, PoolAdmin)
admin.site.register(Prognostication, PoolAdmin)
