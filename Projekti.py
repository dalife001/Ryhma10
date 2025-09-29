import mysql.connector
temp = []

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
         host='127.0.0.1',
         port= 3306,
         database='player',
         user='root',
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
            print("Uusi peli alkaa")

def maat():
 
    sql = f"SELECT name  FROM airport ORDER BY RAND() LIMIT 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for name in tulos: 
        temp.append(name[0]) 

    for counter , value in enumerate(temp, start=1):
        print(counter, value)
        # now updating the list to save the number and the name
    
maat()
