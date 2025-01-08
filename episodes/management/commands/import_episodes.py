from django.core.management.base import BaseCommand
from wagtail.models import Page
from episodes.models import EpisodeIndexPage, EpisodePage
from .rss_feed_processor import create_episode_list

episodes = create_episode_list()

class Command(BaseCommand):
  help = "Imports Welcome to Night Vale episodes from RSS feed"

  def handle(self, *args, **options):
    # delete existing episode index pages and episode pages
    EpisodePage.objects.all().delete()
    EpisodeIndexPage.objects.all().delete()
    # create an episode index page
    home = Page.objects.get(id=3)
    episode_index_page = EpisodeIndexPage(title="Episodes")
    home.add_child(instance=episode_index_page)
    episode_index_page.save_revision().publish()
    # import episode pages
    for episode in episodes:
      episode_page = EpisodePage(
        title=episode["title"],
        episode_number=episode["number"],
        episode_title=episode["title"],
        summary=episode["summary"]
      )
      episode_index_page.add_child(instance=episode_page)
      episode_page.save_revision().publish()
      print("published episode page " + episode["title"])
