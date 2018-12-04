import re

text = "Szukamy cyfr 859 moze tutaj sie jakies 092 ukryly? 666"

# Trenujemy regexera dajac mu instrukcje - czyli nasze wyrazenie regularne.
regexer = re.compile(r"\d\d\d")

# Teraz mowimy regexerowi, zeby szukal tego czego chcemy w podanym tekscie.
# Zwroci pierwszy wynik do zmiennej res.
res = regexer.search(text)

print(text)
print(res.group())

# Jeżeli chcemy aby regexer poszukal wszystkiego co zgadza się z naszymi instrukcjami uzywamy findall
res = regexer.findall(text)
print(res)

# albo
res = regexer.finditer(text)
for match in res:
    print(match.group())
