import mysql.connector
import random
from colorist import Color
import animated_fly

# --- Yhteys tietokantaan ---
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='mkp_db',
    user='root',
    password='root',
    autocommit=True
)

# --- Funktiot ---

def palkinto(arvo):
    pistet=0
    palkinto = random.randint(1,3)
    if palkinto == arvo:
        print("Löysit aarteen saat 5 pistettä!")
        pistet +=5
    return pistet

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
    print(f"\nKäyttäjä {nimi} luotu onnistuneesti!\n")
    return nimi


def hae_kayttaja(nimi):
    sql = "SELECT Name, points FROM player WHERE Name=%s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (nimi,))
    tulos = kursori.fetchone()
    return tulos  # palauttaa (Name, points) tai None


def nayta_lentokentat():
    sql = """
            SELECT a.name, a.ident, c.co2_impact
            FROM airport a 
            LEFT JOIN airport_co2 c
            ON a.ident = c.ident
            ORDER BY RAND()
            LIMIT 3"""

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    lista = []
    for idx, (name, ident, co2) in enumerate(tulos, start=1):
        if co2 is None:
            co2 = 2
        co2_text = (
        "🌱 matala" if co2 == 1 else
        "♻️ keskitaso" if co2 == 2 else
        "🔥 korkea" if co2 == 3 else
        "❓ tuntematon"
        )
        print(f"{Color.RED}{idx}. {name}{Color.OFF} ({co2_text})")
        lista.append((name, ident, co2))
    print()
    return lista

def tallenna_peli(pelaajan_nimi: str, pisteet: int):
    query = """
            UPDATE player
            SET Points = %s
            WHERE Name = %s
            """
    kursori = yhteys.cursor()
    kursori.execute(query, (pisteet, pelaajan_nimi))
    print(f"{Color.CYAN}Pelaajan: {pelaajan_nimi} pisteet: {pisteet} tallennettu.{Color.OFF}")

def pelaa_peli(pelaaja: str, aiemmat_pisteet: int):
    pisteet = aiemmat_pisteet or 15
    piste_arvonta = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    tavoite = random.choice(piste_arvonta)

    print(
        f"Olet aloittelija aaveenmetsästäjä. \n"
        f"Huomasit eräänä päivänä,että järjestö johon kuulut järjestää seminaarin johon haluaisit osallistua. \n"
        f"Suruksesi huomaat, että pääsyvaatimuksena on, että alalta pitää olla jo kokemusta saadakseen siitä kaiken irti."
        f"\nNiinpä päätät alkaa metsästämään aaveita erottuaksesi joukosta, ja saadaksesi kerrottavaa seminaariin. ")
    print(
        f"Aina kun löydät aaveen, saat 10 pistettä."
        f" Jos kentällä ei ole aavetta, menetät 5 pistettä. \n"
        f"Peli päättyy joko silloin, kun saavutat halutun pistemäärän, tai pistemäärä rippuu nollaan.")

    print(f"\n{Color.RED}Hei {pelaaja}{Color.OFF}, "
          f"{Color.YELLOW}sinulla on pisteitä: {pisteet},{Color.OFF} "
          f"{Color.RED}peli alkaa!{Color.OFF}"
          )

    print(f"{Color.MAGENTA}Tavoitteesi on saavuttaa {tavoite} pistettä.{Color.OFF}")
    print(f"{Color.CYAN}Saat 10 pistettä löydettyäsi aaveen, menetät 5 pistettä jos et löydä.{Color.OFF}\n")

    lentokentat = nayta_lentokentat()
    oikea_vastaus = random.choice(lentokentat)
    print()


    while pisteet > 0 and pisteet < tavoite:
        try:
            valinta = int(input(f"Valitse lentokenttä 1-{len(lentokentat)} (0 tallenna ja lopeta): "))
            if valinta == 0:
                tallenna_peli(pelaaja, pisteet)
                break
            if valinta < 0 or valinta > len(lentokentat):
                print(f"Valitse numero väliltä (1-{len(lentokentat)})")
                continue
            print("Siirrytään lentokentälle")
            animated_fly.animate_takeoff()
            print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")

            if lentokentat[valinta - 1] == oikea_vastaus:
                pisteet += 10 + palkinto(valinta)
                print(f"{Color.CYAN}Löysit aaveen! Pisteesi: {pisteet}{Color.OFF}\n")
                lentokentat = nayta_lentokentat()
                oikea_vastaus = random.choice(lentokentat)

            else:
                pisteet -= 5
                print(f"{Color.RED}Et{Color.OFF} löytänyt aavetta ja menetät viisi pistettä.")
                print(f"Pisteesi: {pisteet}\n")
                for idx, kentta in enumerate(lentokentat, start=1):
                    co2 = kentta[2]
                    co2_text = (
                        "🌱 matala" if co2 == 1 else
                        "♻️ keskitaso" if co2 == 2 else
                        "🔥 korkea" if co2 == 3 else
                        "❓ tuntematon"
                    )
                    print(f"{Color.RED}{idx}. {kentta[0]} ({co2_text}){Color.OFF}")
                print("\n")

        except ValueError:
            print("Syötä numero väliltä 1-3!")

    if pisteet <= 0:
        print("Pisteesi tippuivat nollaan, ja peli päättyi. Parempi onni seuraavalla kerralla.")
    elif pisteet >= tavoite:
        print(
            f"{Color.CYAN}Hyvää työtä. Olet kerännyt nyt tarpeeksi kokemusta voidaksesi osallistua seminaariin.{Color.OFF}")


# Pääohjelma
def main():
    flag = True
    aiemmat_pisteet = 0
    nimi = ""
    while flag:
        kys = input("Onko sinulla käyttäjä? (kyllä/ei): ").lower()
        if kys == "kyllä":
            nimi = input("Anna käyttäjänimi: ")
            pelaaja = hae_kayttaja(nimi)
            if pelaaja:
                aiemmat_pisteet = int(pelaaja[1])
                print(f"\nLöytyi aiempi peli!\n"
                      f"Pelaaja: {pelaaja[0]}\n"
                      f"Pisteet: {pelaaja[1]}\n"
                      f"Jatketaan peliä...\n")
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
