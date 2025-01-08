from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class EpisodeIndexPage(Page):
    pass

class EpisodePage(Page):
    parent_page_types = ["episodes.EpisodeIndexPage"]

    episode_number = models.CharField(max_length=250, blank=True)
    episode_title = models.CharField(max_length=250, blank=True)
    summary = models.CharField(max_length=2000, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("episode_number"),
        FieldPanel("episode_title"),
        FieldPanel("summary")
    ]

    search_auto_update = False