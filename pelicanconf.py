#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Barnes'
SITENAME = "Alex's Data Science Blog"
SITEURL = ''
SITETITLE = "Alex's Data Science Blog"
SIDEBAR_DIGEST = 'Data scientist, software engineer, physicist'
PROFILE_IMAGES = 'profile.png'


PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['plugins', 'plugins/pelican-plugins']
PLUGINS = ['ipynb.markup', 'tipue_search']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('Blog', SITEURL),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/abarnes12'),
          ('github', 'https://github.com/abarnes12'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
