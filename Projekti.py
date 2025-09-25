def hae_kayttaja(arvo):
    sql = f"select player from user where player = '{arvo}' "
    if sql == "null":
        print("Käyttäjää ei löydy.")
        return
    else:
        return sql




