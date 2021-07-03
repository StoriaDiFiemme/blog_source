#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Italo Giordani"
SITENAME = "Storia di Fiemme"
SITEURL = ""
DEBUG = True

PATH = "content"

TIMEZONE = "Europe/Paris"
LOCALE = "it_IT.utf8"
DEFAULT_LANG = "it"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

SOCIAL = ()

DEFAULT_PAGINATION = 10

SITEMAP = {
    "format": "xml",
}

THEME = "winnie"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
