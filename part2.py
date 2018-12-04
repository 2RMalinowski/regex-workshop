"""
Dismantle this url into pieces. We want to see protocol, domain and uri in separate groups.
With succesful regex, script should print:
https://wiadomosci.onet.pl/tylko-w-onecie/kuba-wojewodzki-plakalem-po-smolensku-nigdy-nie-bylem-emocjonalnie-tak-blisko/8z5e8jh
https://
wiadomosci.onet.pl
/tylko-w-onecie/kuba-wojewodzki-plakalem-po-smolensku-nigdy-nie-bylem-emocjonalnie-tak-blisko/8z5e8jh

You can only change the REGEX part!

BONUS: Uncomment second string and modify regex to separate port number also.
"""

import re

text = "https://wiadomosci.onet.pl/tylko-w-onecie/kuba-wojewodzki-plakalem-po-smolensku-nigdy-nie-bylem-emocjonalnie-tak-blisko/8z5e8jh"
# text = "http://127.0.0.1:5000/get-boards?user_id=2"  # bonus URL

regexer = re.compile(r".*")  # here in the parenthesis is the famous regex part.
res = regexer.search(text)
if res:
    print(res.group())
    for group in res.groups():
        print(group)
else:
    print("ERROR: Nothing was found.")
