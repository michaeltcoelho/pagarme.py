# coding:utf-8
from pagarme.api import default_api
from pagarme.common import make_url

from .resource import Resource


class Plan(Resource):
    """`Plan`:class: wrapping the REST /plans endpoint
    """
    def create(self):
        response = self.api.post('/plans', self.to_dict())
        self.assign(response)
        return self.success()

    def update(self, attributes=None):
        attributes = attributes or self.to_dict()
        response = self.api.put(make_url('/plans', str(self.id)), data=attributes)
        self.assign(response)
        return self.success()

    def delete(self):
        response = self.api.delete(make_url('/plans', str(self.id)))
        self.assign(response)
        return self.success()

    @classmethod
    def find(cls, plan_id):
        api = default_api()
        url = make_url('/plans', str(plan_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        response = api.get('/plans', params=params)
        return [cls(item) for item in response]
