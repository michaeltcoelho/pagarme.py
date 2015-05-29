# coding:utf-8
import os
import logging
import datetime
import requests
import json

from pagarme.config import __endpoint__, __user_agent__
from pagarme.common import merge_dict, make_url
from pagarme import exceptions

logger = logging.getLogger('pygarme')


class PagarmeApi(object):

    def __init__(self, options=None, **kwargs):
        """`PagarmeApi`:class: Creates an API object
        """
        kwargs = merge_dict(options or {}, kwargs)
        self.endpoint = kwargs.get('endpoint', self.default_endpoint)
        self.apikey = kwargs.get('api_key')
        self.encryption_key = kwargs.get('encryption_key')

        if not self.apikey or not self.encryption_key:
            raise exceptions.NullAPIKeyError('The `api_key` and `encryption_key` must be set.')

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

    def request(self, url, method, data=None, headers=None):
        """Makes a HTTP call, formats response and does error handling.
        """
        http_headers = merge_dict(self.default_headers, headers or {})
        request_data = merge_dict({'api_key': self.apikey}, data or {})

        logger.info('HTTP %s REQUEST TO %s' % (method, url))

        start = datetime.datetime.now()

        try:
            response = requests.request(method=method, url=url, data=json.dumps(request_data),
                                        headers=http_headers)
        except exceptions.BadRequestError as e:
            return json.loads({'errors': e.content})

        duration = datetime.datetime.now() - start

        logger.info('RESPONSE %s DURATION %s.%s' % (response.encoding, duration.seconds,
                                                    duration.microseconds))

        return json.loads(response.content) if response.content else {}

    def get(self, action, params=None, headers=None):
        """Makes a GET request
        """
        return self.request(make_url(self.endpoint, action), method='GET', data=params,
                            headers=headers)

    def post(self, action, data=None, headers=None):
        """Makes a GET request
        """
        return self.request(make_url(self.endpoint, action), method='POST', data=data,
                            headers=headers)

    def put(self, action, data=None, headers=None):
        """Makes a GET request
        """
        return self.request(make_url(self.endpoint, action), method='PUT', data=data,
                            headers=headers)

    def delete(self, action, headers=None):
        """Makes a GET request
        """
        return self.request(make_url(self.endpoint, action), method='DELETE',
                            headers=headers)


__default_api__ = None


def default_api():
    global __default_api__
    if __default_api__ is None:
        try:
            api_key = os.environ["PAGARME_API_KEY"]
            encryption_key = os.environ["PAGARME_ENCRYPTION_KEY"]
        except KeyError:
            raise exceptions.NullAPIKeyError("Required PAGARME_API_KEY and PAGARME_ENCRYPTION_KEY")
        __default_api__ = PagarmeApi(api_key=api_key, encryption_key=encryption_key)
    return __default_api__


def configure(**kwargs):
    global __default_api__
    __default_api__ = PagarmeApi(**kwargs)
    return __default_api__
