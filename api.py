from datetime import datetime


def func():
    now = datetime.now()
    if now.hour > 12:
        return 1
    else:
        return 0
