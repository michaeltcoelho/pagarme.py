# coding:utf-8
from pagarme.api import default_api


class Resource(object):
    """`Resource`:class: allows you to access the json response like a python object.
    The `assign`:method: converts a dictionary to an object.
    The `success`:method: allow you check if the request has been OK.
    The `to_dict`:method: converts the object in a dictionary.
    """
    def __init__(self, attributes=None, api=None):
        self.__dict__['api'] = api or default_api()
        super(Resource, self).__setattr__('__fields__', {})
        self.assign(attributes or {})

    def __getattr__(self, k):
        return self.__fields__.get(k)

    def __setattr__(self, k, v):
        self.__fields__[k] = self.__parse(v)

    def __getitem__(self, k):
        return self.__fields__[k]

    def assign(self, attrs):
        """Merge new attributes
        """
        for k, v in attrs.items():
            setattr(self, k, v)

    def success(self):
        try:
            self.__fields__['errors']
            return False
        except KeyError:
            return True

    def to_dict(self):
        return dict((k, self.__parse(v)) for k, v in self.__fields__.items())

    def __parse(self, obj):
        if isinstance(obj, Resource):
            return obj.to_dict()
        if isinstance(obj, list):
            return list(map(self.__parse, obj))
        if isinstance(obj, dict):
            return Resource(obj)
        else:
            return obj
