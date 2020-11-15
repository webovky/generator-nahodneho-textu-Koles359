#!/usr/bin/env python3

from random import choice, randint

samohlasky = "aeiouy"
souhlasky = "qwrtpsdfghjklzxcvbnm"
pismena = "aeiouyqwrtpsdfghjklzxcvbnm"

while True:
    try:
        pslov = int(input("počet slov  > "))
        filename = input("jméno souboru  > ")
        with open(filename, 'w') as f:
            pocet = 1
            slovo = ""
            delka_radku = 0

            while pocet <= pslov:
                delka_slova = randint(1, 7)
                slovo = ""
                for i in range(delka_slova):
                    if i == 0:
                        slovo += choice(pismena)
                    else:
                        if slovo[i - 1] in samohlasky:
                            slovo += choice(souhlasky)
                        else:
                            slovo += choice(samohlasky)
                slovo += " "
                f.write(slovo)

                delka_radku += len(slovo)
                if 70 <= delka_radku <= 80:
                    f.write("\n")
                    delka_radku = 0

                pocet += 1
        break
    except:
        print("Do počtu slov musíte zadat pouze celé číslo!")
        print("Jméno souboru uveďte ve tvaru např. nahoda.txt .")






