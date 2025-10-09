import random
print(" Olet aloittelija aaveenmetsästäjä. \n Huomasit eräänä päivänä,että järjestö johon kuulut järjestää seminaarin johon haluaisit osallistua. \n Suruksesi huomaat, että pääsyvaatimuksena on, että alalta pitää olla jo kokemusta saadakseen siitä kaiken irti. \n Niinpä päätät alkaa metsästämään aaveita erottuaksesi joukosta, ja saadaksesi kerrottavaa seminaariin. ")
print(" Aina kun löydät aaveen, saat 10 pistettä.Jos kentällä ei ole aavetta, menetät 5 pistettä. \n Peli päättyy joko silloin, kun saavutat halutun pistemäärän, tai pistemäärä rippuu nollaan.")
arvonta = [50,55,60,65,70,75,80,85,90,95,100]
pisteitä= random.choice(arvonta)
print("Tarvitset voittoon", pisteitä, "pistemäärän.")
lentokenttä= input("Anna lentokentän nimi: ")
#if lentokenttä in sql:
print("Siirrytään lentokentälle")
print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")


def onko_aaveita(aaveet):
    return aaveet

pisteet = 15

while pisteet > 0 and pisteet != pisteitä:
    aaveet = random.randint(1, 2)

    if aaveet == 1:
        print("Löysit aaveen ja saat 10 pistettä.")
        pisteet += 10
    if aaveet == 2:
        print("Et löytänyt aavetta ja menetät viisi pistettä.")
        pisteet -= 5
    print("Pisteet ovat nyt", pisteet)

    if pisteet == pisteitä:
        print("Hyvää työtä. Olet kerännyt nyt tarpeeksi kokemusta voidaksesi osallistua seminaariin.")
        break
    elif pisteet == 0:
        print("Pisteesi tippuivat nollaan, ja peli päättyi. Parempi onni seuraavalla kerralla.")
        break

    lentokenttä = input("Anna lentokentän nimi: ")
    # if lentokenttä in sql:
    print("Siirrytään lentokentälle")
    print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")



