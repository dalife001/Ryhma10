import mysql.connector
import random


# --- Yhteys tietokantaan ---
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='player',
    user='root',
    password='P@ssword',
    autocommit=True
)

# --- Funktiot ---

def luo_kayttaja():
    while True:
        nimi = input("Anna käyttäjänimesi (vähintään 3 merkkiä): ")
        if len(nimi) < 3:
            print("Liian lyhyt nimi.")
            continue
        info = input("Lisää tietosi (vähintään 10 merkkiä): ")
        if len(info) < 10:
            print("Liian lyhyt tieto.")
            continue
        break

    sql = "INSERT INTO player (Name, points, Guessed, info) VALUES (%s, %s, %s, %s)"
    kursori = yhteys.cursor()
    kursori.execute(sql, (nimi, 15, 0, info))
    print(f"Käyttäjä {nimi} luotu onnistuneesti!\n")
    return nimi


def hae_kayttaja(nimi):
    sql = "SELECT Name, points FROM player WHERE Name=%s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (nimi,))
    tulos = kursori.fetchone()
    return tulos  # palauttaa (Name, points) tai None


def nayta_lentokentat():
    sql = "SELECT name FROM airport ORDER BY RAND() LIMIT 5"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    lista = [name[0] for name in tulos]
    for idx, lentokentta in enumerate(lista, start=1):
        print(f"{idx}. {lentokentta}")
    print()
    return lista


def pelaa_peli(pelaaja: str, aiemmat_pisteet: int):
    pisteet = aiemmat_pisteet or 15
    print(pisteet)
    piste_arvonta = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    tavoite = random.choice(piste_arvonta)
    print(tavoite)

    print(
        " Olet aloittelija aaveenmetsästäjä. \n Huomasit eräänä päivänä,että järjestö johon kuulut järjestää seminaarin johon haluaisit osallistua. \n Suruksesi huomaat, että pääsyvaatimuksena on, että alalta pitää olla jo kokemusta saadakseen siitä kaiken irti. \n Niinpä päätät alkaa metsästämään aaveita erottuaksesi joukosta, ja saadaksesi kerrottavaa seminaariin. ")
    print(
        " Aina kun löydät aaveen, saat 10 pistettä.Jos kentällä ei ole aavetta, menetät 5 pistettä. \n Peli päättyy joko silloin, kun saavutat halutun pistemäärän, tai pistemäärä tippuu nollaan.")
    print("Tarvitset voittoon", tavoite, "pistemäärän.")

    lentokentat = nayta_lentokentat()
    oikea_vastaus = random.choice(lentokentat)
    print(lentokentat)
    print(oikea_vastaus)

    while True:
        if pisteet >= tavoite:
            print("Hyvää työtä. Olet kerännyt nyt tarpeeksi kokemusta voidaksesi osallistua seminaariin.")
            break
        try:
            valinta = int(input(f"Valitse lentokenttä 1-{len(lentokentat)}: "))
            print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")
            if lentokentat[valinta - 1] == oikea_vastaus:
                pisteet += 10
                print(f"Löysit aaveen! Pisteesi: {pisteet}\n")
                lentokentat = nayta_lentokentat()
                oikea_vastaus = random.choice(lentokentat)
                print(lentokentat)
                print(oikea_vastaus)
                continue

            elif pisteet <= 0:
                print("Pisteesi tippuivat nollaan. Peli päättyi.\n")
                break

            elif lentokentat[valinta-1] != oikea_vastaus:
                pisteet -= 5
                print(f"Ei aavetta täällä. Pisteesi: {pisteet}")

        except ValueError:
            print("Syötä numero väliltä 1-5!")


# --- Pääohjelma ---
def main():
    flag = True
    aiemmat_pisteet = 0
    nimi = ""
    while flag:
        kys = input("Onko sinulla käyttäjä? (kyllä/ei): ").lower()
        if kys == "kyllä":
            nimi = input("Anna käyttäjänimi: ")
            pelaaja = hae_kayttaja(nimi)
            print(pelaaja)
            if pelaaja:
                aiemmat_pisteet = int(pelaaja[1])
                print(f"Löytyi aiempi peli!\n"
                      f"Pelaaja: {pelaaja[0]}\n"
                      f"Pisteet: {pelaaja[1]}\n"
                      f"Jatketaan peliä...")
                flag = False
            else:
                print("Käyttäjää ei löydy. Luodaan uusi.")
                nimi = luo_kayttaja()
                flag = False
        elif kys == "ei":
            nimi = luo_kayttaja()
            flag = False
        else:
            print("Syötä joko kyllä tai ei!")

    pelaa_peli(nimi, aiemmat_pisteet)


if __name__ == "__main__":
    main()
