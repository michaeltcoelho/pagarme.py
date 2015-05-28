# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class Subscription(Resource):
    """`Subscription`:class: wrapping the REST /subscriptions endpoint
    """
    def create(self):
        response = self.api.post('/subscriptions', data=self.to_dict())
        self.assign(response)
        return self.success()

    def update(self, attributes):
        attributes = attributes or self.to_dict()
        url = make_url('/subscriptions', str(self.id))
        response = self.api.put(url, data=attributes)
        self.assign(response)
        return self.success()

    def cancel(self, subscription_id=None):
        if not subscription_id:
            subscription_id = self.id
        url = make_url('/subscriptions', str(subscription_id), '/cancel')
        response = self.api.post(url)
        self.assign(response)
        return self.success()

    def transactions(self, subscription_id=None):
        if not subscription_id:
            subscription_id = self.id
        url = make_url('/subscriptions', str(subscription_id), '/transactions')
        response = self.api.get(url)
        return [Resource(item) for item in response]

    @classmethod
    def find(cls, subscription_id):
        api = default_api()
        url = make_url('/subscriptions', str(subscription_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        response = api.get('/subscriptions', params=params)
        return [cls(item) for item in response]
