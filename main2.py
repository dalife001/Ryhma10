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
    sql = "SELECT name FROM airport ORDER BY RAND() LIMIT 3"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    lista = [name[0] for name in tulos]
    for idx, lentokentta in enumerate(lista, start=1):
        print(f"{Color.RED}{idx}. {lentokentta}{Color.OFF}")
    print()
    return lista


def pelaa_peli(pelaaja: str, aiemmat_pisteet: int):
    pisteet = aiemmat_pisteet or 15
    piste_arvonta = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    tavoite = random.choice(piste_arvonta)

    print(f"\n{Color.RED}Hei {pelaaja}{Color.OFF}, "
          f"{Color.YELLOW}sinulla on pisteitä: {pisteet},{Color.OFF} "
          f"{Color.RED}peli alkaa!{Color.OFF}"
          )

    print(f"{Color.MAGENTA}Tavoitteesi on saavuttaa pistettä.{Color.OFF}")
    print(f"{Color.CYAN}Saat 10 pistettä löydettyäsi aaveen, menetät 5 pistettä jos et löydä.{Color.OFF}\n")

    lentokentat = nayta_lentokentat()
    oikea_vastaus = random.choice(lentokentat)
    print()

    while pisteet > 0 and pisteet < tavoite:
        try:
            valinta = int(input(f"Valitse lentokenttä 1-{len(lentokentat)}: "))
            if valinta < 1 or valinta > len(lentokentat):
                print(f"Valitse numero listan sisällä! (1-{len(lentokentat)}")
                continue

            print("Siirrytään lentokentälle")
            animated_fly.animate_takeoff()
            print("Saavuit lentokentälle, ja aloitat tutkimuksesi.")

            if lentokentat[valinta - 1] == oikea_vastaus:
                print(f"{Color.CYAN}Löysit aaveen! Pisteesi: {pisteet}{Color.OFF}\n")
                pisteet += 10 + palkinto(valinta)
                lentokentat = nayta_lentokentat()
                oikea_vastaus = random.choice(lentokentat)

            else:
                pisteet -= 5
                print("Et löytänyt aavetta ja menetät viisi pistettä.")
                print(f"Pisteesi: {pisteet}\n")
                for idx, kentta in enumerate(lentokentat, start=1):
                    print(f"{Color.RED}{idx}. {kentta}{Color.OFF}")
                print("\n")

        except ValueError:
            print("Syötä numero väliltä 1-3!")

    if pisteet <= 0:
        print("Pisteesi tippuivat nollaan, ja peli päättyi. Parempi onni seuraavalla kerralla.")
    elif pisteet >= tavoite:
        print(
            f"{Color.RED}Hyvää työtä. Olet kerännyt nyt tarpeeksi kokemusta voidaksesi osallistua seminaariin.{Color.OFF}")

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
            if pelaaja:
                aiemmat_pisteet = int(pelaaja[1])
                print(f"\nLöytyi aiempi peli!\n"
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
