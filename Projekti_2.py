import mysql.connector
import random



def onko_hiilineutraali(arvo):
    neutraalit =["Oslo Gardermoen","Stockholm Arlanda","Kööpenhamina Kastrup","Amsterdam Schiphol",
    "Dallas–Fort Worth","San Diego International", "Delhi Indira Gandhi International",
    "Mumbai Chhatrapati Shivaji Maharaj International" ,"Doha Hamad International","Christchurch  International Airport"]

    for i in arvo:
        if i in neutraalit:
            print(f"{i} on hiilineutraali")
        else:
            print(f"{i} ei ole hiilineutraali")



def tallennus(nimi,pisteet):
    sql = f"UPDATE player SET points = '{pisteet}' WHERE Name = '{nimi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    yhteys.commit()
    print(f"Tallennettu")
    kursori.close()


def create_kayttaja():
    Username = input(" Anna käyttäjänimesi: ")
    if len(Username) < 3:
        print("Käyttäjänimen tulee olla vähintään 3 merkkiä pitkä.")
    infomation = input("Lisää tietosi: ")
    if len(infomation) < 5:
        print("Tietojen tulee olla vähintään 10 merkkiä pitkä.")
    sql = f"INSERT INTO player (Name,points,Guessed, info) VALUES ('{Username}','{0}','{0}','{infomation}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    print("Käyttäjä luotu onnistuneesti")
    return Username


def hae_kayttaja(arvo):
    sql = f"select name from player where name = '{arvo}' "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos[0]



def tiedon_haku(arvo):
    sql = f"select points from player where name = '{arvo}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos[0]




yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='peli',
    user='root',
    password='helsinki',
    autocommit=True
)


def main():
    tunnus, pisteet = kysy()
    peli(tunnus,pisteet)

def maat():
    lista=[]
    sql = f"SELECT name FROM airport ORDER BY RAND() LIMIT 3"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for name in tulos:
        lista.append(name[0])
    return lista






def kysy():
    pelaaja_pisteet= 0
    ksy = str(input("Onko sinulla käyttäjä: kyllä/ei ")).lower()

    while True:
        if ksy == "kyllä":
            kayttaja = str(input("Anna käyttäjä: "))
            pelaaja_nimi = hae_kayttaja(kayttaja)

            if pelaaja_nimi == "null":
                print("Käyttäjää ei löydy.")
                pelaaja_nimi =create_kayttaja()
                pelaaja_pisteet+= 15
                return pelaaja_nimi,pelaaja_pisteet

            elif pelaaja_nimi != kayttaja:
                print("Virhe")
                continue
            else:
                kysymys_arvo = str(input("Haluatko jatkaa peliä: kyllä/ei ").lower())

                if kysymys_arvo == "kyllä":
                    pelaaja_pisteet = tiedon_haku(kayttaja)
                    return pelaaja_nimi,pelaaja_pisteet          #Tämä kohta ei toimi

                elif kysymys_arvo == "ei":
                    print("Luo uusi käyttäjä")
                    pelaaja_nimi = create_kayttaja()
                    pelaaja_pisteet +=15
                    return pelaaja_nimi,pelaaja_pisteet

        elif ksy == "ei":
            pelaaja_nimi = create_kayttaja()
            pelaaja_pisteet +=15
            return pelaaja_nimi,pelaaja_pisteet



def peli(pelaaja:str,pistet:int):
    pisteet = 0
    arvonta = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    pisteita = random.choice(arvonta)
    pisteet += pistet
    print(
        " Olet aloittelija aaveenmetsästäjä. \n Huomasit eräänä päivänä,että järjestö johon kuulut järjestää seminaarin johon haluaisit osallistua. \n Suruksesi huomaat, että pääsyvaatimuksena on, että alalta pitää olla jo kokemusta saadakseen siitä kaiken irti. \n Niinpä päätät alkaa metsästämään aaveita erottuaksesi joukosta, ja saadaksesi kerrottavaa seminaariin. ")
    print(
        " Aina kun löydät aaveen, saat 10 pistettä.Jos kentällä ei ole aavetta, menetät 5 pistettä. \n Peli päättyy joko silloin, kun saavutat halutun pistemäärän, tai pistemäärä rippuu nollaan.")
    print("Tarvitset voittoon", pisteita, "pistemäärän.")
    kentat= maat()

    while True:
        onko_hiilineutraali(kentat)
        lentokentta = int(input(f"Valitse lentokenttä: 1.{kentat[0]},2.{kentat[1]},3.{kentat[2]}: "))
        print("Siirrytään lentokentälle")
        print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")
        oikea_vastaus = random.randint(1,3)
        palkinto = random.randint(1,3)
        kentat.clear()
        kentat= maat()
        if lentokentta == oikea_vastaus:
            print("Löysit aaveen ja saat 10 pistettä.")
            pisteet += 10
            print(f"Pisteet ovat nyt {pisteet}")
            if pisteet >= pisteita:
                print("Hyvää työtä. Olet kerännyt nyt tarpeeksi kokemusta voidaksesi osallistua seminaariin.")
                tallennus(pelaaja, pisteet)
                break
            elif oikea_vastaus == palkinto:
                print("Löysit palkinnon saat 5 pistettä.")
                pisteet += 5
                print(f"Pisteet ovat nyt {pisteet}")
            elif pisteet == (pisteita - 5):
                print("Melkein perillä.")

        elif lentokentta != oikea_vastaus:
            print("Et löytänyt aavetta ja menetät viisi pistettä.")
            pisteet -= 5
            print(f"Pisteet ovat nyt {pisteet}")
            if pisteet <= 0:
                print("Pisteesi tippuivat nollaan, ja peli päättyi. Parempi onni seuraavalla kerralla.")
                tallennus(pelaaja,pisteet)
                break
            else:
                continue




if __name__ == "__main__":
    main()
