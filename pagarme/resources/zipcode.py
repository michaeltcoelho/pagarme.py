# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class ZipCode(Resource):
    """`ZipCode`:class: wrapping the REST /zipcodes endpoint
    """
    @classmethod
    def find(cls, zipcode):
        api = default_api()
        url = make_url('/zipcodes', str(zipcode))
        return cls(api.get(url))
