import mysql.connector
import random
lista = []

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

def lisaa_kayttaja(arvo):
    sql = f"insert into users(player) values '{arvo}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return




yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='foot',
         password='2004',
         autocommit=True
         )

kys = input("Onko sinulla käyttäjä: kyllä/ei")
if kys == "kyllä":
    kayttaja = input("Anna käyttäjä: ")
    pelaaja_nimi = hae_kayttaja(kayttaja)

    if pelaaja_nimi == "null":
        print("Käyttäjää ei löydy.")
        # funktio tähän

    else:
        kysymys_arvo = str(input("Haluatko jatkaa peliä: kyllä/ei"))

        if kysymys_arvo == "kyllä":
            pelaaja_pisteet = tiedon_haku()

        elif kysymys_arvo == "ei":
            #funktio tähän

elif kys == "ei":
    uusi_kayttaja = input("Anna nimi: ")
    kayttaja_uusi = lisaa_kayttaja(uusi_kayttaja)

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
    oikea_vastaus =  # funktio tähän 
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

def maat():
 
    sql = f"SELECT name  FROM airport ORDER BY RAND() LIMIT 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for name in tulos: 
        lista.append(name[0]) 

    for counter , value in enumerate(lista, start=1):
        print(counter, value)
        # now updating the list to save the number and the name
    
maat()

