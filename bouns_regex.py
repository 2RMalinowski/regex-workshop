import re

with open("resource/bonus.txt") as f:
    text = f.read()

print("\033[H\033[2J")
print(text)
print("\nZnajdz wszystkie valid ID numbers")

correct = False
valid_answer = ['BCD345765', 'FRG354211', 'QQQ111111']

while not correct:

    inpt = input("\ndaj regexa: ")
    print("\033[H\033[2J")

    try:
        regex = re.compile(eval(f"r'{inpt}'"))
        res = [match.group() for match in regex.finditer(text)]
    except:
        res = []
        print("Cos poszlo nie tak z regexem :(")
    if res != valid_answer:
        print(text)
        print("Sprobuj jeszcze raz!\n")
        print("\nZnajdz wszystkie valid ID numbers")
        print(f"Regex znalazł : {res} \npowinen: {valid_answer}")
    else:
        correct = True
        print(f"Regex znalazł : {res}")
        print("Gratki!")
