from django.urls import path

from . import views

urlpatterns = [
    path("", views.FeedListView.as_view(), name="feed"),
    path("subscribe/<int:feed_id>/", views.Subscribe.as_view(), name="subscribe"),
    path("unsubscribe/<int:feed_id>/", views.Unsubscribe.as_view(), name="unsubscribe"),
]