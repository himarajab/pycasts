from django.db import models
from users.models import User

class Feed(models.Model):
    title = models.CharField(max_length=70)
    user =models.ManyToManyField(User)
    def __str__(self) -> str:
        return f"{self.title}"