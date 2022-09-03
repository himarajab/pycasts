from django.views.generic import ListView
from .models import Episode
from feed.models import Feed
from pprint import pprint
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin,ListView):
    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs):
        user = self.request.user
        feeds = Feed.objects.filter(user=user)
        episodes=Episode.objects.filter(feed__in=feeds)
        context = super().get_context_data(**kwargs)
        context["episodes"] = episodes
        return context