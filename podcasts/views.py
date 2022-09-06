from podcasts.models import Episode
from pprint import pprint
from rest_framework import generics, permissions
from podcasts.serializers import EpisodeSerializer
from feed.models import Feed


class EpisodeList(generics.ListAPIView):
    """
    List all Episode
    """
    serializer_class = EpisodeSerializer
    permission_classes = (
		permissions.IsAuthenticated,
	)
    def get_queryset(self):
        user = self.request.user
        feeds = Feed.objects.filter(user=user)
        queryset_filtered = Episode.objects.filter(feed__in=feeds)
        return queryset_filtered