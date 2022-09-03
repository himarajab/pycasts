from django.db import models
from feed.models import Feed

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)
    feed = models.ForeignKey(Feed,  on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.title}"