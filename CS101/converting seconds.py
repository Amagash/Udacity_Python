# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#
def is_plural(value, unit):
    if value == 1:
        return unit
    return str(unit)+"s"

def convert_seconds(seconds):
    hours = int(seconds/(3600))
    minutes = int((seconds%(3600))/60)
    secondes = seconds - (hours*3600 + minutes*60)
    return str(hours) + " " + is_plural(hours, "hour") + ", " + str(minutes) + " " + is_plural(minutes, "minute") + ", " + str(secondes) + " " + is_plural(secondes, "second")


#
# hours = 0
# print is_plural(hours, "hour")


print convert_seconds(3600)
print convert_seconds(60)

print convert_seconds(3661)
# >>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
# >>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
# >>> 2 hours, 1 minute, 1.7 seconds