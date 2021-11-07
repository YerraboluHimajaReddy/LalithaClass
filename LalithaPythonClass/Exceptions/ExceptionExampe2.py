# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# The entry is a
# Oops! <class 'ValueError'> occurred.
# Next entry.
#
# The entry is 0
# Oops! <class 'ZeroDivisionError'> occurred.
# Next entry.
#
# The entry is 2
# The reciprocal of 2 is 0.5
