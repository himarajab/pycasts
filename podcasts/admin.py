from django.contrib import admin

from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "pub_date")