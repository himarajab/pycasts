from django.urls import path

from . import views

urlpatterns = [
    path("episode-list", views.EpisodeList.as_view(), name="episode-list"),
]