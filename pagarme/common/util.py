# coding:utf-8
import re


def merge_dict(data, *args):
    """Merge any number of dictionaries
    """
    results = {}
    for current in (data,) + args:
        results.update(current)
    return results


def make_url(url, *paths):
    """Joins individual URL strings together, and returns a single string.
    """
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url
