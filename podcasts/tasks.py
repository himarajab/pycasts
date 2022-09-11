# Standard Library
from pprint import pprint

# Third Party
import feedparser
from dateutil import parser
from celery import shared_task
from celery.utils.log import get_task_logger

# Models
from podcasts.models import Episode
from feed.models import Feed


logger = get_task_logger(__name__)
    
def save_new_episodes(feed):
    """Saves new episodes to the database.

    Checks the episode GUID agaist the episodes currently stored in the
    database. If not found, then a new `Episode` is added to the database.

    Args:
        feed: requires a feedparser object
    """
    title = feed.channel.title
    image = feed.channel.image["href"]
    custom_feed, _ = Feed.objects.get_or_create(title=title)
    for item in feed.entries:
        if not Episode.objects.filter(guid=item.guid).exists():
            episode = Episode(
                title=item.title,
                feed_id=custom_feed.id,
                description=item.description,
                pub_date=parser.parse(item.published),
                link=item.link,
                image=image,
                name=title,
                guid=item.guid,
            )
            episode.save()


@shared_task()
def hello_celery():
    logger.info("hello_celery task just ran.")


@shared_task()
def fetch_realpython_episodes():
    """Fetches new episodes from RSS for the Real Python Podcast."""
    logger.info("hello_celery task just ran.")
    _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(_feed)


@shared_task()
def fetch_talkpython_episodes():
    """Fetches new episodes from RSS for the Talk Python to Me Podcast."""
    _feed = feedparser.parse("https://talkpython.fm/episodes/rss")
    save_new_episodes(_feed)