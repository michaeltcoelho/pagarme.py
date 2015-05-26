# coding:utf-8


class MetaData(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def to_dict(self):
        metadata = {}
        for k, v in self.kwargs:
            metadata['metadata[%s]' % k] = v
        return metadata


class CustomerMetaData(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def to_dict(self):
        metadata = {}
        for k, v in self.kwargs.items():
            key = 'customer[%s]' % k
            if isinstance(v, dict):
                for ks, vs in v.items():
                    metadata[key + ('[%s]' % ks)] = vs
            else:
                metadata[key] = v
        return metadata