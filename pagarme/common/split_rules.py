# coding:utf-8


class SplitRules(object):
    """`SplitRules`:class:
    """
    def __init__(self, rules):
        self.rules = rules

    def to_dict(self):
        if isinstance(self.rules, list):
            return dict((k, rule) for k, rule in enumerate(self.rules))
        else:
            return {0: self.rules}