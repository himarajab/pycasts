from django.views.generic import ListView


from .models import Feed


class FeedListView(ListView):

    template_name = "feed.html"

    model = Feed