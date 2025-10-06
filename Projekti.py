import mysql.connector
import random
lista = []
from other import aarin_avaus_kysymys
from other import aarin_vastaus
aarin_vastaus()
aarin_avaus_kysymys()
def main():
    
    kysy()
    hae_kayttaja()
    tiedon_haku()
    create_kayttaja()
    maat()
    arvonta()
    yhteys.close()

def create_kayttaja():
    Username = input(" Anna käyttäjänimesi: ")
    if len(Username) < 3:
        print("Käyttäjänimen tulee olla vähintään 3 merkkiä pitkä.")
    infomation = input("Lisää tietosi: ")
    if len(infomation) < 5:
        print("Tietojen tulee olla vähintään 10 merkkiä pitkä.")
    sql = f"INSERT INTO player (Name,points,Guessed, info) VALUES ('{Username }','{15}','{0}','{infomation}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    print("Käyttäjä luotu onnistuneesti")
    return Username

def hae_kayttaja(arvo):
    sql = f"select player from user where player = '{arvo}' "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def tiedon_haku(arvo):
    sql = f"select points from user where player = '{arvo}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos





yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='player',
         user='root',
         password='2004',
         autocommit=True
         )

def maat():
 
    sql = f"SELECT name  FROM airport ORDER BY RAND() LIMIT 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for name in tulos: 
        lista.append(name[0]) 

    for counter , value in enumerate(lista):
        print()
maat()

def  kysy():
     ksy = input("Onko sinulla käyttäjä: kyllä/ei")
     if ksy == "kyllä":
            kayttaja = input("Anna käyttäjä: ")
            pelaaja_nimi = hae_kayttaja(kayttaja)
    
            if pelaaja_nimi == "null":
                print("Käyttäjää ei löydy.")
                create_kayttaja()
    
            else:
                kysymys_arvo = str(input("Haluatko jatkaa peliä: kyllä/ei"))
    
                if kysymys_arvo == "kyllä":
                    pelaaja_pisteet = tiedon_haku(kayttaja)
    
                elif kysymys_arvo == "ei":
                    print("Luo uusi käyttäjä")
                    ksy == "ei"
                    create_kayttaja()
     else:
            print("Luo uusi käyttäjä")
            ksy == "ei"
            create_kayttaja()

print(lista)
pisteet = 15
arvonta = [50,55,60,65,70,75,80,85,90,95,100]
pisteita = random.choice(arvonta)
print(" Olet aloittelija aaveenmetsästäjä. \n Huomasit eräänä päivänä,että järjestö johon kuulut järjestää seminaarin johon haluaisit osallistua. \n Suruksesi huomaat, että pääsyvaatimuksena on, että alalta pitää olla jo kokemusta saadakseen siitä kaiken irti. \n Niinpä päätät alkaa metsästämään aaveita erottuaksesi joukosta, ja saadaksesi kerrottavaa seminaariin. ")
print(" Aina kun löydät aaveen, saat 10 pistettä.Jos kentällä ei ole aavetta, menetät 5 pistettä. \n Peli päättyy joko silloin, kun saavutat halutun pistemäärän, tai pistemäärä rippuu nollaan.")
print("Tarvitset voittoon", pisteita, "pistemäärän.")
while True:
    lentokentta = input(f"Valitse lentokenttä: 1.{lista[0]},2.{lista[1]},3.{lista[2]},4.{lista[3]}5.{lista[4]} ")
    print("Siirrytään lentokentälle")
    print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")
    oikea_vastaus = random.choice(range(len(lista))) 
    print(oikea_vastaus)
    lista.clear()
    maat()
    if lentokentta == oikea_vastaus:
        print("Löysit aaveen ja saat 10 pistettä.")
        pisteet+=10
        print(f"Pisteet ovat nyt {pisteet}")
        if pisteet == pisteita:
            print("Hyvää työtä. Olet kerännyt nyt tarpeeksi kokemusta voidaksesi osallistua seminaariin.")
            break
        else:
            continue
    elif lentokentta != oikea_vastaus:
        print("Et löytänyt aavetta ja menetät viisi pistettä.")
        pisteet-=5
        print(f"Pisteet ovat nyt {pisteet}")
        if pisteet == 0:
            print("Pisteesi tippuivat nollaan, ja peli päättyi. Parempi onni seuraavalla kerralla.")
            break
        else:
            continue

def arvonta():
    
    real = random.choice(lista)
    gues=  input("Arvaa lentokenttä: ") 
    if gues == real:
         print("Oikein arvattu")
    else:
            print("Väärin arvattu")
            print(f"Oikea vastaus oli {real}")
    
    return real

main()