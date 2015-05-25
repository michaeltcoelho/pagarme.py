# coding:utf-8
from pagarme.api import default_api
from pagarme.resource import Resource
from pagarme.util import make_url


class Plan(Resource):
    """plans class wrapping the REST /plans endpoint
    """
    def create(self):
        response = self.api.post('/plans', self.to_dict())
        self.assign(response)
        return self.success()

    def update(self, params=None):
        params = params or self.to_dict()
        response = self.api.post(make_url('/plans', str(self.id)), params=params)
        self.assign(response)
        return self.success()

    def delete(self):
        response = self.api.delete(make_url('/plans', str(self.id)))
        self.assign(response)
        return self.success()

    @classmethod
    def find(cls, resource_id):
        api = default_api()
        url = make_url('/plans', str(resource_id))
        return cls(api.get(url))

    @classmethod
    def all(cls, count=10, page=1):
        api = default_api()
        params = {'count': count, 'page': page}
        responses = api.get('/plans', params=params)
        return [cls(item) for item in responses]