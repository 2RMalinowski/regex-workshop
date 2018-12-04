import re

text = "https://wiadomosci.onet.pl/tylko-w-onecie/kuba-wojewodzki-plakalem-po-smolensku-nigdy-nie-bylem-emocjonalnie-tak-blisko/8z5e8jh"

regexer = re.compile(r".*")
res = regexer.search(text)
if res:
    print(res.group())
    for group in res.groups():
        print(group)
else:
    print("ERROR: Nothing was found.")
