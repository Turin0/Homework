import inspect


def introspection_info(obj):
    dict_ = {}
    list_1 = []
    list_2 = []
    for attr in dir(obj):
        if callable(attr):
            list_2.append(attr)
        else:
            list_1.append(attr)
    dict_.update(dict(type=type(obj), attributes=list_1, method=list_2, module=inspect.getmodule(obj)))

    return dict_


class MyClass:
    def __init__(self, at_1, at_2):
        self.at_1 = at_1
        self.at_2 = at_2

    def sum_(self):
        return self.at_1 + self.at_2


h_w = MyClass(20, 30)
print(introspection_info(h_w))
