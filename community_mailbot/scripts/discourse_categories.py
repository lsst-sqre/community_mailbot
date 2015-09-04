# encoding: utf-8
"""
List categories and their IDs in a Discourse forum.
"""

import os
from argparse import ArgumentParser
from urllib.parse import urljoin
import requests


def main():
    args = parse_args()

    params = {}
    if args.key is not None:
        params['api_key'] = args.key
    if args.user is not None:
        params['api_username'] = args.user

    url = urljoin(args.url, 'site.json')
    r = requests.get(url, params=params)
    r.raise_for_status()
    site_feed = r.json()
    for c in site_feed['categories']:
        print(c['id'], c['name'])


def parse_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        '--key',
        default=os.getenv('DISCOURSE_KEY', None),
        help='Discourse API key')
    parser.add_argument(
        '--user',
        default=os.getenv('DISCOURSE_KEY', None),
        help='Discourse API user')
    parser.add_argument(
        '--url',
        default='http://community.lsst.org',
        help='Base URL of the discourse forum')
    return parser.parse_args()


if __name__ == '__main__':
    main()
