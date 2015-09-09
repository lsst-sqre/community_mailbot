# encoding: utf-8
"""
Test the contentpipe module.
"""

import unittest
from urllib.parse import urlparse

from community_mailbot.contentpipe import make_absolute_link


class TestMakeAbsoluteLink(unittest.TestCase):

    def setUp(self):
        self.base_url_parts = urlparse('http://community.lsst.org',
                                       scheme='http')

    def test_absolute_discourse_link(self):
        orig_link = '//community.lsst.org/c/dm/dm-notifications'
        correct_link = 'http://community.lsst.org/c/dm/dm-notifications'

        self.assertEqual(
            make_absolute_link(orig_link, self.base_url_parts),
            correct_link)

    def test_other_domain_absolute_link(self):
        orig_link = '//github.com'
        correct_link = 'http://github.com'

        self.assertEqual(
            make_absolute_link(orig_link, self.base_url_parts),
            correct_link)

    def test_relative_discourse_link(self):
        orig_link = '/users/jsick'
        correct_link = 'http://community.lsst.org/users/jsick'

        self.assertEqual(
            make_absolute_link(orig_link, self.base_url_parts),
            correct_link)
