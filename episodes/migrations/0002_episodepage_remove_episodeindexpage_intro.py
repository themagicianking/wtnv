# Generated by Django 5.1.4 on 2025-01-08 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("episodes", "0001_initial"),
        ("wagtailcore", "0094_alter_page_locale"),
    ]

    operations = [
        migrations.CreateModel(
            name="EpisodePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("episode_number", models.CharField(blank=True, max_length=250)),
                ("episode_title", models.CharField(blank=True, max_length=250)),
                ("summary", models.CharField(blank=True, max_length=250)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.RemoveField(
            model_name="episodeindexpage",
            name="intro",
        ),
    ]
