from .models import Feed
from pprint import pprint
from rest_framework import generics, permissions
from feed.serializers import FeedSerializer


class FeedListView(generics.ListAPIView):
    """
    List all Feed
    """
    serializer_class = FeedSerializer
    def get_queryset(self):
        queryset = Feed.objects.all()
        return queryset
    

    

def subscribe(request,feed_id):
    user_id = request.user.id
    feed = Feed.objects.get(id = feed_id)
    updated=feed.user.add(user_id)    
    return redirect("homepage")

def unsubscribe(request,feed_id):
    user_id = request.user.id
    feed = Feed.objects.get(id = feed_id)
    feed.user.remove(user_id)    
    return redirect("homepage")
    