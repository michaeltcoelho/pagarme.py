# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class Card(Resource):
    """`Card`:class: wrapping the REST /cards endpoint
    """
    def create(self):
        response = self.api.post('/cards', data=self.to_dict())
        self.assign(response)
        return self.success()

    @classmethod
    def find(cls, card_id):
        api = default_api()
        url = make_url('/cards', str(card_id))
        return cls(api.get(url))
