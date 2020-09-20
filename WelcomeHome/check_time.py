import datetime

def is_time_between(begin_time, end_time, check_time=None):

    check_time = check_time or datetime.datetime.now().time()
    print(check_time)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

print(is_time_between(datetime.time(10,30), datetime.time(16,30)))

print(is_time_between(datetime.time(22,0), datetime.time(4,00)))