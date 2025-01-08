import feedparser
import re

wtnv_rss_url = "https://feeds.nightvalepresents.com/welcometonightvalepodcast"
feed = feedparser.parse(wtnv_rss_url).entries
episodes = []
real_titles = r"[0-9]*[A-Z]*\s-\s.*|[0-9]*\s-\s.*|Bonus\sEpisode\s[0-9]*\s-\s"


def parse_full_title(full_title):
    return full_title.split(" - ")


def parse_summary(full_summary):
    results = re.split(r"<p>|<\/p>", full_summary)
    results = list(filter(None, results))
    return results[0]


def parse_entry(entry):
    if re.match(real_titles, entry.title):
        num, title = parse_full_title(entry["title"])
    else:
        num, title = "X", entry.title
    summary = parse_summary(entry["summary"])

    return {"number": num, "title": title, "summary": summary}


def create_episode_list():
    for entry in feed:
        episode = parse_entry(entry)
        episodes.append(episode)
    return episodes
