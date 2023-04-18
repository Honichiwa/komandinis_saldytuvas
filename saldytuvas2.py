import os

os.system("cls")

produktai = {}
shopping_list = {}
receptas = {}


def perziureti_saldytuva():
    os.system("cls")

    if list(produktai.keys()) != []:
        for indeksas, reiksme in enumerate(produktai):
            indeksas += 1
            print(indeksas, ".", reiksme, produktai[reiksme])
    else:
        print("Saldytuvas tuscias")


while True:
    os.system("cls")

    print("-------[ Šaldytuvas ]-------")
    print("1: Įdėti produktus")
    print("2: Išimti produktus")
    print("3: Suskaičiuoti")
    print("4: Produktu patikra receptui")
    print("0: Išeiti")

    pasirinkimas = input("Pasirinkite: ")

    if pasirinkimas > str(5) or pasirinkimas < str(0):  # neteisingas pasirinkimas
        while True:
            os.system("cls")
            print(
                "!!Neteisingas pasirinkimas, spauskite ENTER ir bandykite dar kartą!!"
            )
            back = input("")
            break

    if pasirinkimas == "0":
        os.system("cls")
        print("-------[ Viso gero ]-------")
        break

    if pasirinkimas == "1":  # pirmas pasirinkimas
        os.system("cls")
        print("-------[ Produkto įdėjimas į šaldytuvą ]-------")
        perziureti_saldytuva()
        produktas = input("\nĮveskite produktą: ")  # ivedame produkto pavadinima
        produkto_kiekis = float(
            input("\nĮveskite produkto svorį: ")
        )  # ivedame produkto kieki
        produktai[
            produktas
        ] = produkto_kiekis  # kiekvienas ivestas produktas sukuria zodyno nauja keys ir produkto kiekis sukuria to keys values

        while True:
            pasirinkimas_3 = input(" Įveskite 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "2":  # antras pasirinkimas
        os.system("cls")
        perziureti_saldytuva()
        print("-------[ Produkto išimimas iš šaldytuvo ]-------")

        while True:
            isimamas_produktas = input(" Įveskite 0 grįžti į MENIU \n\u2794 ")
            if isimamas_produktas == "0":
                break
            else:
                isimamas_kiekis = float(input("Isimamas kiekis: "))
                esamas_kiekis = produktai[isimamas_produktas]
                esamas_kiekis -= isimamas_kiekis
                produktai[isimamas_produktas] = esamas_kiekis
                if esamas_kiekis <= 0:
                    del produktai[isimamas_produktas]

    if pasirinkimas == "3":  # trecias pasirinkimas
        os.system("cls")
        perziureti_saldytuva()
        print("-------[ Produktų svorio skaičiavimas ]-------")

        bendras_kiekis = 0
        for produktas in produktai.values():
            bendras_kiekis += produktas
        print(f"Visų produktų svoris: {bendras_kiekis}")

        while True:
            pasirinkimas_3 = input("Įveskite 0 grįžti į MENIU \n\u2794")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "4":  # ketvirtas pasirinkimas
        os.system("cls")
        perziureti_saldytuva
        print("-------[ Produktu patikra receptui ]-------")
        while True:
            print("1: Įdėti produktus")
            print("2: Išimti produktus")
            print("3: Shopping list")
            print("0: Iseiti")
            pasirinkimas_meniuke = input("Pasirinkite: ")
            if pasirinkimas_meniuke == "0":
                break
            if pasirinkimas_meniuke == "1":
                os.system("cls")
                print("-------[ Produkto įdėjimas į receptu knyga ]-------")
                perziureti_saldytuva()
                produktas = input(
                    "\nĮveskite produktą: "
                )  # ivedame produkto pavadinima
                produkto_kiekis = float(
                    input("\nĮveskite produkto svorį: ")
                )  # ivedame produkto kieki
                receptas[
                    produktas
                ] = produkto_kiekis  # kiekvienas ivestas produktas sukuria zodyno nauja keys ir produkto kiekis sukuria to keys values

                while True:
                    pasirinkimas_3 = input(" Įveskite 0 grįžti į MENIU \n\u2794 ")
                    if pasirinkimas_3 == "0":
                        break

            pasirinkimas_3 = input(" Įveskite 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break
