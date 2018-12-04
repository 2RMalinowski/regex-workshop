"""
This can be tricky. Or not. We have a log file and we want to get all the IP addresses from it.
Sounds simple, right?

Script will tell you if its correct or not. It's smart.

You can only change the REGEX part!
"""

import re
from part3validation import validate_output

with open("resource/log.txt") as f:
    text = f.read()

regexer = re.compile(r".*")  # here in the parenthesis is the famous regex part.
res = [match.group() for match in regexer.finditer(text)]
if res:
    for match in res:
        print(match)
else:
    print("ERROR: Nothing was found.")

print(validate_output(res))
