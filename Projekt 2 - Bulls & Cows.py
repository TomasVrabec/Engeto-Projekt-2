import random

# oddelovac = "-"*40
# print(f"""
# Hi there!
# {oddelovac}
# I've generated a random 4 digit number for you.
# Let's play a bulls and cows game.
# {oddelovac}"""
# )

#generování náhodného čísla
cislice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while cislice[0] == 0:
    random.shuffle(cislice)

hadane_cislo = cislice[:4]

print(hadane_cislo)

# def zadavani_cisla():
#     while True:
#         vstup = input("Enter a number: ")
#         if vstup