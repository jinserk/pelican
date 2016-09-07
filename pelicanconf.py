#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jinserk Baik'
SITENAME = u"Shinbee's Home"
SITEURL = 'https://jinserk.github.io'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['gravatar', 'render_math']

# theme
STATIC_PATHS = ['images', 'pdfs']
THEME = "../pelican-themes/pure"

COVER_IMG_URL = "images/main.jpg"

# sidebar
SOCIAL = (
    ('envelope-o', 'mailto:jinserk.baik@gmail.com'),
    ('linkedin', 'http://www.linkedin.com/in/jinserk'),
    ('twitter', 'https://twitter.com/jinserk'),
    ('facebook', 'https://www.facebook.com/jinserk'),
    ('github', 'https://github.com/jinserk'),
    ('stack-overflow', 'http://stackoverflow.com/users/2392124/jinserk'),
)

