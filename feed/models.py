from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self) -> str:
        return f"{self.title}"