import mysql.connector

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