import random

oddelovac = "-"*40
print(f"""
Hi there!
{oddelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{oddelovac}"""
)

#generování náhodného čísla
cislice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while cislice[0] == 0:
    random.shuffle(cislice)

hadane_cislo = cislice[:4]


print("vygenerované číslo: ", hadane_cislo)

def uzivatelovi_tipy():
    while True:
        try:
            vstup = int(input("Enter a number: "))
            if vstup in range(1000, 10000):
                break
            else:
                print("Incorrect input...")
        except:
            pass

    a = str(vstup)
    tip = list()
    for i in a:
        tip.append(int(i))
    print("uživatelův tip: ", tip)
    return tip

def vyhodnoceni ():
    tip = uzivatelovi_tipy()
    # bull - číslice na stejném místě
    bull = 0
    for i in range(0,4):
        if tip[i] == hadane_cislo[i]:
            bull += 1

    # cows - číslice na jiném místě
    cow = 0
    for i in range(0, 4):
        if tip[i] in hadane_cislo and tip[i] != hadane_cislo[i]:
            cow += 1


    # výpis výsledku
    if bull == 4:
        print("Correct, you've guessed the right number")
    elif bull == 1 and cow == 1:
        print(bull, "bull, ", cow, "cow")
    elif bull == 1 and cow != 1:
        print(bull, "bull, ", cow, "cows")
    elif bull != 1 and cow == 1:
        print(bull, "bulls, ", cow, "cow")
    else:
        print(bull, "bulls, ", cow, "cows")


def hra():
    while x := True:
        if vyhodnoceni() != "Correct, you've guessed the right number":
          vyhodnoceni()
        break

hra()