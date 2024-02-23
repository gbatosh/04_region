from datetime import datetime
def a():
    a = datetime.now().replace(microsecond=0)
    x = datetime(year = 1970, month = 1, day = 24, hour = 23, minute = 54, second = 12)
    print((a-x).total_seconds())
a()