from django.shortcuts import  render, redirect
from django.views.generic import ListView
from .models import Feed
from .models import Feed
from pprint import pprint

class FeedListView(ListView):

    template_name = "feed.html"

    model = Feed
    

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
    