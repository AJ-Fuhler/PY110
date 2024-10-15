MINUTES_IN_DAY = 1440

def after_midnight(time):
    if time == '24:00':
        return 0
    hours = int(time[:2])
    minutes = int(time[3:])

    total = (hours * 60) + minutes

    return total

def before_midnight(time):
    if time == '24:00' or time == '00:00':
        return 0
    
   
    hours = int(time[:2])
    
    
    minutes = int(time[3:])

    total = (hours * 60) + minutes

    return MINUTES_IN_DAY - total





print(after_midnight("00:01") == 1)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True


HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hours, minutes = [int(unit) for unit in time_str.split(":")]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0

    return delta_minutes

print(after_midnight("00:01") == 1)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True