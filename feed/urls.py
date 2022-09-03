from django.urls import path

from . import views

urlpatterns = [
    path("", views.FeedListView.as_view(), name="feed"),
    path("<int:feed_id>/", views.subscribe, name="subscribe"),
    path("unsubscribe/<int:feed_id>/", views.unsubscribe, name="unsubscribe"),
]