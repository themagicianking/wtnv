from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
import os
import feedparser
import re

rss_data = "/Users/tpl1122_1/Desktop/projects/wtnv/episodes/rss-feed.txt"

with open(rss_data, 'r') as file_obj:
    first_char = file_obj.read(1)

    if not first_char:
        wtnv_rss_url = "https://feeds.nightvalepresents.com/welcometonightvalepodcast"
        feed = feedparser.parse(wtnv_rss_url)
        file = open(rss_data, "a")
        file.write(str(feed))
        file.close()
    else:
        print("text file created already.")

class EpisodeIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]