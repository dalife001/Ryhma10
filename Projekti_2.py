def tiedon_haku(arvo):
    sql = f"select  from user where player = '{arvo}'"

kysymys_arvo = str(input("Haluatko jatkaa peliä: kyllä/ei"))

if kysymys_arvo == "kyllä":
    pelaaja_pisteet = tiedon_haku()

elif kysymys_arvo == "ei":
    #funktio kutsu tähän