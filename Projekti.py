def hae_kayttaja(arvo):
    sql = f"select player from user where player = '{arvo}' "
    if sql == "null":
        print("Käyttäjää ei löydy.")
        return
    else:
        return sql




yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='foot',
         password='2004',
         autocommit=True
         )