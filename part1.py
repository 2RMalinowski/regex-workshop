"""
Find the date format and create three groups: DD, MM, YYYY.
With succesful regex, script should print:
24/09/2018
24
09
2018

You can only change the REGEX part!
"""

import re


text = "24/09/2018 to byla dobra data nie to co 1/8/1520"

regexer = re.compile(r".*")  # here in the parenthesis is the famous regex part.
res = regexer.search(text)
print(res.group())
for group in res.groups():
    print(group)
