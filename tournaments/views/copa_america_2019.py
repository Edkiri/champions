"""Copa américa views."""

# Django
from django.views.generic import ListView, DetailView

# Models
from tournaments.models import Tournament, TournamentGroup

class HomeView(ListView):
  """Home view."""

  model = Tournament

  template_name = "home.html"

class TournamentDetailView(DetailView):

  model = Tournament
  template_name = "tournament-detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if TournamentGroup.objects.filter(tournament=self.object, phase="GS"):
      groups = TournamentGroup.objects.filter(tournament=self.object)
      context['groups'] = groups.filter(phase="GS")
      context['quarters'] = groups.get(phase="QF")
      context['semis'] = groups.get(phase="SF")
      context['third_and_fourth'] = groups.get(phase="TF")
      context['final'] = groups.get(phase="F")
      return context
    return context