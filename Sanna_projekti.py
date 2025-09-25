import random
print(" Olet aloittelija aaveenmetsästäjä. \n Huomasit eräänä päivänä,että järjestö johon kuulut järjestää seminaarin johon haluaisit osallistua. \n Suruksesi huomaat, että pääsyvaatimuksena on, että alalta pitää olla jo kokemusta saadakseen siitä kaiken irti. \n Niinpä päätät alkaa metsästämään aaveita erottuaksesi joukosta, ja saadaksesi kerrottavaa seminaariin. ")
print(" Aina kun löydät aaveen, saat 10 pistettä.Jos kentällä ei ole aavetta, menetät 5 pistettä. \n Peli päättyy joko silloin, kun saavutat halutun pistemäärän, tai pistemäärä rippuu nollaan.")
arvonta = random.randint(50, 100)
print("Tarvitset voittoon", arvonta, "pistemäärän.")
lentokenttä= input("Anna lentokentän nimi: ")
#if lentokenttä in sql:
print("Siirrytään lentokentälle")
print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")


