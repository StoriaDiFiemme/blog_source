#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Italo Giordani"
SITENAME = "Storia di Fiemme"
SITESUBTITLE = "Una finestra aperta sulla Valle di Fiemme"
SITEURL = ""
DEBUG = True

PATH = "content"

TIMEZONE = "Europe/Paris"
LOCALE = "it_IT.utf8"
DEFAULT_LANG = "it"

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = "atom.xml"
TAG_FEED_ATOM = "categories/{slug}/atom.xml"
CATEGORY_FEED_ATOM = "category/{slug}/atom.xml"

ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = ARCHIVES_URL + "index.html"

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

SOCIAL = []

DEFAULT_PAGINATION = 10

SITEMAP = {
    "format": "xml",
}

THEME = "winnie"

QUOTES = []

STATIC_PATHS = [
    "extra/CNAME",
    "extra/robots.txt",
]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
