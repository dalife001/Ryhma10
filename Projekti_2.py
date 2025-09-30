from Projekti import yhteys
from Projekti import temp
from random import choice
from random import randint
def usercreateer():
    Username = input(" Anna käyttäjänimesi: ")
    if len(Username) < 3:
        print("Käyttäjänimen tulee olla vähintään 3 merkkiä pitkä.")
    infomation = input("Lisää tietosi: ")
    if len(infomation) < 5:
        print("Tietojen tulee olla vähintään 10 merkkiä pitkä.")
    sql = f"INSERT INTO player (Name,points,Guessed, info) VALUES ('{Username }','{15}','{0}','{infomation}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    print("Käyttäjä luotu onnistuneesti")



def guessing():
   gues=  input("Arvaa lentokenttä: ") ## if the real name is guessed
     