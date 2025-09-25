import mysql.connector

def hae_kayttaja(arvo):
    sql = f"select player from user where player = '{arvo}' "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos




yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='foot',
         password='2004',
         autocommit=True
         )

pelaaja_nimi = hae_kayttaja()

if pelaaja_nimi == "null":
    print("Käyttäjää ei löydy.")
    #funktio tähän

else:
    kysymys_arvo = str(input("Haluatko jatkaa peliä: kyllä/ei"))

    if kysymys_arvo == "kyllä":
        pelaaja_pisteet = tiedon_haku()

    elif kysymys_arvo == "ei":

        # funktio kutsu tähän
