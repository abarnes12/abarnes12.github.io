#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = 'Alex Barnes'
SITENAME = "Alex's Data Science Blog"
SITETITLE = "Alex's Data Science Blog"
SIDEBAR_DIGEST = 'Data scientist, software engineer, physicist'
PROFILE_IMAGES = 'profile.png'

SITEURL = 'https://abarnes12.github.io'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['plugins', 'plugins/pelican-plugins']
PLUGINS = ['ipynb.markup', 'tipue_search']


#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
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



DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
