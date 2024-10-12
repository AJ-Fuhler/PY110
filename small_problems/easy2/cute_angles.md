Write a function that takes a floating point number representing an angle
between 0 and 360 degrees and returns a string representing that angle in
degrees, minutes, and seconds. You should use a degree symbol (°) to represent
degrees, a single quote (') to represent minutes, and a double quote (") to
represent seconds. There are 60 minutes in a degree, and 60 seconds in a
minute.

1. Understanding the Problem:

Convert a floating point number to a string reprenting an angle between 0 and
360 degrees.

Input: float
Output: string representing float in degrees

Requirements:
  
  Explicit:
  - degree should be represented by °
  - minutes should be represented by '
  - seconds should be represented by "
  
  Implicit:
  - if whole number, minutes and seconds need to be represented as two 0's each
  - every degree needs to be followed by \""

2. Examples and Test Cases:

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

3. Data Structures

- floats as input data, maybe conversion to integers to get whole degree
- string as output

4. Algorithm

- given 'float_degree'
- 'SECONDS_IN_DEGREE' = 3600
- 'whole_degree' = convert 'float_degree' to rounded down integer
- 'decimal_degree' = remainder of 'float_degree' - 'whole_degree'
- 'total_seconds' = 'SECONDS_IN_DEGREE' / 'decimal_degree'
- 'minutes' = quotient of 'total_seconds' / 60
- 'seconds' = remainder of the above quotient (use divmod method to extract both)
- convert 'minutes' and 'seconds' to strings
- if 'minutes' or 'seconds' is less than 10, prepend a '0' to them.
- return a string in the right format, interpolating all necessary values to them.