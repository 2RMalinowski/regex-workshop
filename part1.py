import re

text = "24/09/2018 to byla dobra data nie to co 1/8/1520"

regexer = re.compile(r".*")
res = regexer.search(text)
print(res.group())
for group in res.groups():
    print(group)
