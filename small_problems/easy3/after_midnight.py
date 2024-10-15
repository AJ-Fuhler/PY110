MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_WEEK = 7
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY
MINUTES_IN_WEEK = MINUTES_IN_DAY * DAYS_IN_WEEK

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday"]

def convert_and_prepend_zero_if_needed(time_unit):
    if time_unit < 10:
        return '0' + str(time_unit)
    else:
        return time_unit

def time_of_day(total_minutes):
    day = (total_minutes % MINUTES_IN_WEEK) // MINUTES_IN_DAY
    
    total_hours, minutes = divmod(total_minutes, MINUTES_IN_HOUR)
    current_hours = total_hours % HOURS_IN_DAY
    current_hours = convert_and_prepend_zero_if_needed(current_hours)
    minutes = convert_and_prepend_zero_if_needed(minutes)

    return f'{DAYS[day]}, {current_hours}:{minutes}'

print(time_of_day(-12000))   # True



