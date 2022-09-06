from rest_framework import serializers
from podcasts.models import Episode


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = ( 
                  'title', 
                  'description',
                  'pub_date',
                  'link',
                  'image',
                  'name',
                  'guid',
                  'feed',
                  )