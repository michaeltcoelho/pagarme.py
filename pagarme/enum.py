# coding:utf-8


class Enum(set):
    """Enum - from http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
    """
    def __getattr__(self, name):
        if name in self:
            return str(name).lower()
        raise AttributeError

payment_method = Enum(['CREDIT_CARD', 'BOLETO'])