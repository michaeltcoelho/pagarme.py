# coding:utf-8


class NullAPIKeyError(Exception):
    """Raised when the api_key is None
    """


class ConnectionError(Exception):
    def __init__(self, response, content=None, message=None):
        self.response = response
        self.content = content
        self.message = message

    def __str__(self):
        message = "Failed."
        if hasattr(self.response, 'status_code'):
            message += 'Response status code: %s' % self.response.status_code
        if hasattr(self.response, 'reason'):
            message += 'Response reason: %s' % self.response.reason
        if self.content is not None:
            message += 'Error message: %s' % (str(self.content))
        return message


class ClientError(ConnectionError):
    """4xx Exceptions Error
    """


class BadRequestError(ClientError):
    """400 Error Code
    """


class MetaDataInstanceError(Exception):
    """Raised when a metadata object passed to a resource
     is not a instance of `MetaData` class.
    """


class CustomerInstanceError(Exception):
    """Raised when a customer metadata object passed to a resource
     is not a instance of `CustomerMetaData` class.
    """
