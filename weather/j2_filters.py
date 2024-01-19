from datetime import datetime

import pendulum


def j2_strftime(value, format='%Y-%m-%d') -> str:
    if isinstance(value, datetime):
        return value.strftime(format)

    return pendulum.parse(value).strftime(format)


