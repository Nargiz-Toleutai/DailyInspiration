import datetime


def get_current_date():
    return datetime.datetime.now().strftime("%d.%m.%Y")
