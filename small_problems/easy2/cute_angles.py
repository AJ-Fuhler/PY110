DEGREE = "\u00B0"

def dms(float_degree):
    SECONDS_IN_DEGREE = 3600
    whole_degree = int(float_degree)
    decimal_degree = float_degree - whole_degree
    total_seconds = int(SECONDS_IN_DEGREE * decimal_degree)
    minutes, seconds = divmod(total_seconds, 60)
    
    if minutes < 10:
        minutes = f'0{minutes}'
    else:
        minutes = str(minutes)
    
    if seconds < 10:
        seconds = f'0{seconds}'
    else:
        seconds = str(seconds)

    return f"""{whole_degree}{DEGREE}{minutes}'{seconds}\""""


print(dms(30))
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")