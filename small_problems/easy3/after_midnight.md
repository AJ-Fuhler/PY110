 The time of day can be represented as the number of minutes before or after
 midnight. If the number of minutes is positive, the time is after midnight. If
 the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns
the time of day in 24-hour format (hh:mm). Your function should work with any
integer input.

1. Understanding the Problem

Input: integer representing total minutes in the day before or after midnight.
Output: String representing that time of day in a 24-hour format

Requirements:

  Explicit:
  - The integer given can be either positive or negative
  - The function should work with ANY integer input.
  - The output string should have this format: (hh:mm)
  - You may not use Python's datatime module.
  - disregard Daylight Savings, Standard Time etc.

  Implicit:
  - The total minutes in a day is 1440
  - If the integer exceeds this number, we should move to the next midnight
    until we've exhausted the input integer.


2. Examples and Test Cases

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

3. Data Structures

- Integers: to hold the number of hours and total minutes

4. Algorithm

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY (1440)

- given the TOTAL_MINUTES
- hours = quotient of TOTAL_MINUTES / MINUTES_IN_HOUR
- minutes = remainder of TOTAL_MINUTES / MINUTES_IN_HOUR
- final_hours = remainder of hours / HOURS_IN_DAY
- if final_hours < 10, turn into string and prepend a '0' to it
- else, only turn into string
- convert minutes into a string
- join and return final_hours and minutes together with a delimiter of ':'
