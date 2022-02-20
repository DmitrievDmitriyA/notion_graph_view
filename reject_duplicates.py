from collections.abc import Mapping
from collections.abc import Iterable
from collections import UserDict


# A special override that provides dictionary that restricts duplicate keys
class Dict(UserDict):
    def __init__(self, inp=None):
        if isinstance(inp, dict):
            super(Dict, self).__init__(inp)
        else:
            super(Dict, self).__init__()
            if isinstance(inp, (Mapping, Iterable)):
                si = self.__setitem__
                for k, v in inp:
                    si(k, v)

    def __setitem__(self, k, v):
        try:
            self.__getitem__(k)
            raise ValueError("duplicate key '{0}' found".format(k))
        except KeyError:
            super(Dict, self).__setitem__(k, v)
