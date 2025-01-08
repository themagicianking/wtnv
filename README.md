# wtnv

A project for Techtonica using Welcome to Night Vale's RSS feed as practice for reading text files with python and displaying them.

## Setup Instructions

1. Run ``pip install wagtail`` to install wagtail locally.
2. Navigate into the project's directory and run ``pip install -r requirements.txt``.
3. To create the SQLite database, run ``python manage.py migrate``.
4. To create an admin user for the site, run ``python manage.py createsuperuser`` and follow the prompts.
5. Run ``python manage.py runserver``.
6. Once the server starts, you should be able to access the site locally at  http://127.0.0.1:8000. You should also be able to edit the site's pages by clicking on the wagtail icon in the corner of the page and logging in with the superuser credentials you created.
7. Should you decide to edit the episode page template and you want to regenerate the site with the updated template, run ``manage.py import_episodes`` and the current episode index and episode pages will be deleted and recreated with your new template.

## Further Reference

- This project uses Wagtail. Their docs can be found [here](https://docs.wagtail.org/en/stable/index.html).
- The script I used to generate episode pages is a modified version of [this recipe](https://gist.github.com/tomdyson/ef8c2f684620b84feaddfd7454e09647) created by @[tomdyson](https://gist.github.com/tomdyson) who also cofounded Wagtail. It was a huge help, thanks!