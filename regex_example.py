import re

text = "Szukamy cyfr 859 moze tutaj sie jakies ukryly?"

# Trenujemy regexera dajac mu instrukcje - czyli nasze wyrazenie regularne.
regexer = re.compile(r"\d\d\d")

# Teraz mowimy regexerowi, zeby szukal tego czego chcemy w podanym tekscie. Zwroci to do zmiennej res.
res = regexer.search(text)

print(text)
print(res.group())
