# coding:utf-8
import os
import logging
import datetime
import requests
import json

from pagarme.config import __endpoint__, __user_agent__
from pagarme import exceptions, util

logger = logging.getLogger('pygarme')


class PagarmeApi(object):

    def __init__(self, **kwargs):
        """Creates an API object
        """
        self.endpoint = kwargs.get('endpoint', self.default_endpoint)
        self.apikey = kwargs.get('api_key')
        self.encryption_key = kwargs.get('encryption_key')
        if not self.apikey:
            raise exceptions.NullAPIKeyError('The `api_key` must be set.')

    @property
    def default_endpoint(self):
        """Returns the default endpoint
        """
        return __endpoint__

    @property
    def default_user_agent(self):
        """Returns the api user agent
        """
        return __user_agent__

    @property
    def default_headers(self):
        """Returns the default headers
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": self.default_user_agent
        }

    # TODO: error handling
    def request(self, url, method, body=None, headers=None):
        """Makes a HTTP call, formats response and does error handling.
        """
        http_headers = util.merge_dict(self.default_headers, headers or {})
        request_data = util.merge_dict({'api_key': self.apikey}, body or {})

        logger.info('HTTP %s REQUEST TO %s' % (method, url))

        start = datetime.datetime.now()

        try:
            response = requests.request(method=method, url=url, data=json.dumps(request_data), headers=http_headers)

            print response
        except exceptions.BadRequestError as e:
            return json.loads({'error': e.content})

        duration = datetime.datetime.now() - start

        logger.info('RESPONSE %s DURATION %s.%s' % (response.content, duration.seconds, duration.microseconds))

        return json.loads(response.content.decode('utf-8')) if response.content else {}

    def get(self, action, params=None, headers=None):
        """Makes a GET request
        """
        return self.request(util.make_url(self.endpoint, action), method='GET',
                            body=params or {}, headers=headers or {})

    def post(self, action, params=None, headers=None):
        """Makes a GET request
        """
        return self.request(util.make_url(self.endpoint, action), method='POST',
                            body=params or {}, headers=headers or {})

    def put(self, action, params=None, headers=None):
        """Makes a GET request
        """
        return self.request(util.make_url(self.endpoint, action), method='PUT',
                            body=params or {}, headers=headers or {})

    def delete(self, action, headers=None):
        """Makes a GET request
        """
        return self.request(util.make_url(self.endpoint, action), method='DELETE', headers=headers or {})


__default_api__ = None


def default_api():
    global __default_api__
    if __default_api__ is None:
        try:
            api_key = os.environ["PAGARME_API_KEY"]
            encryption_key = os.environ["PAGARME_ENCRYPTION_KEY"]
        except KeyError:
            raise exceptions.NullAPIKeyError("Required PAGARME_API_KEY")
        __default_api__ = PagarmeApi(api_key=api_key, encryption_key=encryption_key)
    return __default_api__


def config(**kwargs):
    global __default_api__
    __default_api__ = PagarmeApi(**kwargs)
    return __default_api__