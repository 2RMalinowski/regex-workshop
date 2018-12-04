import re

with open("resource/log.txt") as f:
    text = f.read()

regexer = re.compile(r".*")
res = regexer.finditer(text)
if res:
    for match in res:
        print(match.group())
else:
    print("ERROR: Nothing was found.")
