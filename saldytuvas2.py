import os
import json
import logging

os.system("cls")

with open("saldytuvo_turinys.json", "r", encoding="utf-8") as data:
    produktai = json.load(data)

shopping_list = {}
receptas = {}

logeris = logging.basicConfig(filename='logeris.log', encoding='UTF-8', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
logging.info('Programos atidarymas')



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def saldytuvo_papildymas():
    
    produktas = input("\nĮveskite produktą: ")  # ivedame produkto pavadinima
    try:
        produkto_kiekis = float(input("\nĮveskite produkto svorį: "))  # ivedame produkto kieki
    except ValueError:
        print('Įveskite skaičiumi')
        logging.debug('Bloga įvestis')
        produkto_kiekis = float(input("\nĮveskite produkto svorį: "))  # ivedame produkto kiek
    if produktas in produktai:
        kiekis = produktai[produktas]
        produkto_kiekis += kiekis
    logging.info(f"Įdėtas produktas: {produktas}, kiekis: {produkto_kiekis}")
    return produktas, produkto_kiekis

def perziureti_saldytuva():
    clear()

    if list(produktai.keys()) != []:
        for indeksas, reiksme in enumerate(produktai):
            indeksas += 1
            print(indeksas, ".", reiksme, produktai[reiksme])
    else:
        print("Saldytuvas tuščias")

def perziureti_recepta():
    clear()

    if list(receptas.keys()) != []:
        for indeksas, reiksme in enumerate(receptas):
            indeksas += 1
            print(indeksas, ".", reiksme, receptas[reiksme])
    else:
        print("Receptas tuščias")

def perziureti_shopping_list():
    clear()

    if list(shopping_list.keys()) != []:
        for indeksas, reiksme in enumerate(shopping_list):
            indeksas += 1
            print(indeksas, ".", reiksme, shopping_list[reiksme])
    else:
        print("Shoping list'as tuščias")

while True:
    clear()

    print("-------[ Šaldytuvas ]-------")
    print("1: Įdėti produktus")
    print("2: Išimti produktus")
    print("3: Suskaičiuoti")
    print("4: Produktų patikra receptui")
    print("0: Išeiti")

    try:
        pasirinkimas = input("Pasirinkite: ")
    except ValueError: 
        if pasirinkimas > str(5) or pasirinkimas < str(0):
            print("!!Neteisingas pasirinkimas, spauskite ENTER ir bandykite dar kartą!!")
    if pasirinkimas == "0":
        clear()
        print("-------[ Viso gero ]-------")
        with open('saldytuvo_turinys.json', 'w', encoding='utf-8') as file:
            json.dump(produktai, file)
            logging.info('Išėjimas iš programos')
        break

    if pasirinkimas == "1":  # pirmas pasirinkimas
        clear()
        print("-------[ Produkto įdėjimas į šaldytuvą ]-------")
        perziureti_saldytuva()
        produktas, produkto_kiekis = saldytuvo_papildymas()
        produktai[produktas] = produkto_kiekis

        while True:
            pasirinkimas_3 = input(" Įveskite 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "2":  # antras pasirinkimas
        clear()
        perziureti_saldytuva()
        print("-------[ Produkto išimimas iš šaldytuvo ]-------")

        while True:
            isimamas_produktas = input("Įveskite 0 grįžti į MENIU \n\u2794 arba parašykite produktą, kurį norite išimti: ")
            if isimamas_produktas == "0":
                break
            else:
                try:
                    isimamas_kiekis = float(input("Isimamas kiekis: "))
                except ValueError:
                    print('Įveskite skaičiumi')
                    logging.debug('Bloga įvestis')
                    isimamas_kiekis = float(input("Isimamas kiekis: "))
                esamas_kiekis = produktai[isimamas_produktas]
                esamas_kiekis -= isimamas_kiekis
                produktai[isimamas_produktas] = esamas_kiekis
                if esamas_kiekis <= 0:
                    del produktai[isimamas_produktas]
                logging.info(f"Išimtas produktas: {isimamas_produktas}, kiekis: {isimamas_kiekis}")

    if pasirinkimas == "3":  # trecias pasirinkimasą
        clear()
        print("-------[ Produktų svorio skaičiavimas ]-------")
        perziureti_saldytuva()

        bendras_kiekis = 0
        for produktas in produktai.values():
            bendras_kiekis += produktas
        print(f"Visų produktų svoris: {bendras_kiekis}")

        while True:
            pasirinkimas_3 = input("Įveskite 0 grįžti į MENIU \n\u2794")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "4":  # ketvirtas pasirinkimas
        clear()
        print("-------[ Produktu patikra receptui ]-------")
        perziureti_saldytuva()
        
        while True:
            recepto_produktas = input('Įveskite recepto produktą: ')
            recepto_kiekis = int(input('Įveskite produkto kiekį: '))
            receptas[recepto_produktas] = recepto_kiekis
            
            tolimesnis_parinkimas = int(input('Jei norite toliau pildyti receptą(1), tęsti(0): '))
            if tolimesnis_parinkimas == 1:
                continue
            if tolimesnis_parinkimas == 0:
                break
        
        porcijos = int(input('Įveskite porcijų kiekį: '))
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
        
        print('Receptui pagaminti reikės vienai porcijai: ')
        perziureti_shopping_list()
        
        perziureti_saldytuva()
        porcijos_perteklius = []
        for produktas in receptas:
            if produktas in produktai:
                kartojasi = produktai[produktas] / receptas[produktas]
                porcijos_perteklius.append(kartojasi)
        if min(porcijos_perteklius) > 1:
            perteklius = min(porcijos_perteklius)
            print(f'Įmanoma pagaminti dar tiek porcijų: {perteklius}')
        
        while True:
            pasirinkimas_3 = input("Įveskite 0 grįžti į MENIU \n\u2794")
            if pasirinkimas_3 == "0":
                break