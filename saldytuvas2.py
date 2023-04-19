import os

os.system("cls")

produktai = {}
shopping_list = {}
receptas = {}


def saldytuvo_papildymas():
    produktas = input("\nĮveskite produktą: ")  # ivedame produkto pavadinima
    produkto_kiekis = float(
        input("\nĮveskite produkto svorį: ")
    )  # ivedame produkto kieki
    return produktas, produkto_kiekis


def perziureti_saldytuva():
    os.system("cls")

    if list(produktai.keys()) != []:
        for indeksas, reiksme in enumerate(produktai):
            indeksas += 1
            print(indeksas, ".", reiksme, produktai[reiksme])
    else:
        print("Saldytuvas tuscias")


def perziureti_recepta():
    os.system("cls")

    if list(receptas.keys()) != []:
        for indeksas, reiksme in enumerate(receptas):
            indeksas += 1
            print(indeksas, ".", reiksme, receptas[reiksme])
    else:
        print("Receptas tuscias")


def perziureti_shopping_list():
    os.system("cls")

    if list(shopping_list.keys()) != []:
        for indeksas, reiksme in enumerate(shopping_list):
            indeksas += 1
            print(indeksas, ".", reiksme, shopping_list[reiksme])
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
        produktas, produkto_kiekis = saldytuvo_papildymas()
        produktai[produktas] = produkto_kiekis

        while True:
            pasirinkimas_3 = input(" Įveskite 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "2":  # antras pasirinkimas
        os.system("cls")
        perziureti_saldytuva()
        print("-------[ Produkto išimimas iš šaldytuvo ]-------")

        while True:
            isimamas_produktas = input(
                "Įveskite 0 grįžti į MENIU \n\u2794 arba parašykite produktą, kurį norite išimti: "
            )
            if isimamas_produktas == "0":
                break
            else:
                isimamas_kiekis = float(input("Isimamas kiekis: "))
                esamas_kiekis = produktai[isimamas_produktas]
                esamas_kiekis -= isimamas_kiekis
                produktai[isimamas_produktas] = esamas_kiekis
                if esamas_kiekis <= 0:
                    del produktai[isimamas_produktas]

    if pasirinkimas == "3":  # trecias pasirinkimasą
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
        perziureti_saldytuva()
        print("-------[ Produktu patikra receptui ]-------")

        while True:
            recepto_produktas = input("Įveskite recepto produktą: ")
            recepto_kiekis = int(input("Įveskite produkto kiekį: "))
            receptas[recepto_produktas] = recepto_kiekis

            tolimesnis_parinkimas = int(
                input("Jei norite toliau pildyti receptą(1), tęsti(0): ")
            )
            if tolimesnis_parinkimas == 1:
                continue
            if tolimesnis_parinkimas == 0:
                break

        porcijos = int(input("Įveskite porcijų kiekį: "))
        perziureti_recepta()

        for produktas_1 in receptas:
            kiekis_1 = receptas[produktas_1] * porcijos
            if produktas_1 in produktai:
                trukumas = produktai[produktas_1] - kiekis_1
                if trukumas < 0:
                    shopping_list[produktas_1] = abs(trukumas)
            elif not produktas_1 in produktai:
                shopping_list[produktas_1] = kiekis_1
            else:
                trukumas = produktai[produktas_1] - kiekis_1
                shopping_list[produktas_1] = trukumas

        print("Receptui pagaminti reikės vienai porcijai: ")
        perziureti_shopping_list()

        perziureti_saldytuva()
        porcijos_perteklius = []
        for produktas in receptas:
            if produktas in produktai:
                kartojasi = produktai[produktas] / receptas[produktas]
                porcijos_perteklius.append(kartojasi)
        if min(porcijos_perteklius) > 1:
            perteklius = min(porcijos_perteklius)
            print(f"Įmanoma pagaminti dar tiek porcijų: {perteklius}")
