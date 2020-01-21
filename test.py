from test.api import *


def change_time(h):
    time = datetime.now().replace(hour=h)

    def f():
        if time.hour > 12:
            return 1
        else:
            return 0

    return f


def test():
    func = change_time(6)
    assert func() == 1
    assert func() == 0


test()
