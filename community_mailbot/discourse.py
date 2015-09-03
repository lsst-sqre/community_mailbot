# encoding: utf-8
"""
Tools for reading the JSON API from a Discourse site.
"""

import os
from urllib.parse import urljoin
import json

import requests


class CategoryFeed(object):
    """JSON feed from a specific category.

    Parameters
    ----------
    category_id : int
        Category identifier.
    base_url : str
        Root URL of the Discourse forum.
    key : str, optional
        Discourse API key, needed for working with private categories.
    user : str, optional
        Discourse API username, needed for working with private categories.
    """
    def __init__(self, category_id, base_url, key=None, user=None):
        super().__init__()
        self._category_id = category_id
        self._base_url = base_url
        self._key = key
        self._user = user

        self._feed = self._fetch_feed()

    @property
    def url(self):
        """JSON feed URL."""
        return urljoin(self._base_url, 'c/{0}.json'.format(self._category_id))

    def _fetch_feed(self):
        """Get the category's JSON feed and parse it into a Python dict."""
        params = {}
        if self._key is not None:
            params['api_key'] = self._key
        if self._user is not None:
            params['api_user'] = self._user
        r = requests.get(self.url, params=params)
        r.raise_for_status()  # can raise requests.exceptions.HTTPError
        return r.json()


class TopicFeed(object):
    """JSON feed from a Discourse topic.

    Parameters
    ----------
    category_id : int
        Category identifier.
    base_url : str
        Root URL of the Discourse forum.
    key : str, optional
        Discourse API key, needed for working with private categories.
    user : str, optional
        Discourse API username, needed for working with private categories.
    """
    def __init__(self, topic_slug, base_url, key=None, user=None):
        super().__init__()
        self._slug = topic_slug
        self._base_url = base_url
        self._key = key
        self._user = user

        self._feed = self._fetch_feed()

    @property
    def url(self):
        """JSON feed URL."""
        # Because requests is not adding these parameters to my URL!
        url = urljoin(self._base_url, 't/{0}.json'.format(self._slug))
        if (self._key is not None) and (self._user is not None):
            url += '?api_key={key}&api_user={user}'.format(key=self._key,
                                                           user=self._user)
        return url

    def _fetch_feed(self):
        """Get the topic's JSON feed and parse it into a Python dict."""
        # Surprisingly requests is not adding these parameters to my URL!
        # params = {}
        # if self._key is not None:
        #     params['api_key'] = self._key
        # if self._user is not None:
        #     params['api_user'] = self._user
        # print(params)
        # r = requests.get(self.url, params=params)
        r = requests.get(self.url)
        print(r.url)
        r.raise_for_status()  # can raise requests.exceptions.HTTPError
        return r.json()

    @property
    def slug(self):
        """Slug (URL shortname) of the topic."""
        return self._slug

    @property
    def html_url(self):
        """Topic HTML URL."""
        url = urljoin(self._base_url, 't/{0}'.format(self._slug))
        return url

    @property
    def datetime_iso(self):
        """ISO datetime string of first post in topic"""
        return self._feed['post_stream']['posts'][0]['created_at']

    @property
    def category_id(self):
        """The topic's category (``int`` ID)."""
        return self._feed['category_id']

    @property
    def title(self):
        """The topic's title."""
        return self._feed['fancy_title']

    @property
    def first_post_content(self):
        """Content of the topic's first post, as HTML (latest revision)."""
        return self._feed['post_stream']['posts'][0]['cooked']

    @property
    def first_post_author_real_name(self):
        """Display name of the topic's original poster."""
        return self._feed['post_stream']['posts'][0]['display_username']
