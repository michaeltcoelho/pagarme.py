# coding:utf-8

__all__ = [
    'payment_methods',
    'transaction_states'
]


class Enum(set):
    """`Enum`:class: from
    http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
    """
    def __getattr__(self, name):
        if name in self:
            return str(name).lower()
        raise AttributeError


payment_methods = Enum([
    'CREDIT_CARD',
    'BOLETO'
])

transaction_states = Enum([
    'PROCESSING',
    'AUTHORIZED',
    'PAID',
    'REFUNDED',
    'WAITING_PAYMENT',
    'PENDING_REFUND',
    'REFUSED'
])
