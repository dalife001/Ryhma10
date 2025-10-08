import random
from chess import chess1
from Projekti import lista
second_list = lista.copy()
from Projekti import pisteet
# this is extra stuff to get more points
potion = False
def aarin_vastaus():
    
    treasure = random.randint(1,5)
   
    if treasure == 4:
         print("u got a bonus heart")
         
         if potion == True:
             print("since the potion is active u get 2x effect from the treasure" )
             potion = False
         small_pouch()
    elif treasure == 3:
        print("Trap activated, you lose 1 heart")
        if potion == True:
             print("since the potion is active u get 2x effect from the treasure" )
             potion = False
        small_pouch()
    if treasure == 2:
        print("You potion next chess will give u 2x")
        doublex()

    elif treasure == 1:
        print("You found a small pouch, you that will help u find the ghost next round")
    
        if potion == True:
             print("since the potion is active u get 2x effect from the treasure" )
             potion = False 
        small_pouch()
    else:
        print("You got blinded, u cant  see the ghost next round")

def asciianimater():
     ## this one animates the heart in the game depending if the user get extra heart or lose one 
    ##  and  second animates the trap chest   plus if the user opens the chess or not 
    pass

def  aarin_avaus_kysymys():
    print(chess1)
    print("Hei, onneksi olkoon, löysit aarteen, haluatko avata sen? kyllä/ei")
    vastaus = str(input()).lower()
    if vastaus == "kyllä":
        asciianimater()
        aarin_vastaus()
    elif vastaus == "ei":
        print("okei, jatketaan matkaa")
def doublex():
    global potion
    potion = True
    print("Onneksi olkoon! Taikajuoma on aktivoitu! saat 2x vaikutuksen seuraavasta aarteesta")
def small_pouch():
    # idk how this will work on the project but it will help u find the ghost next round
  for i in range(len(second_list)-1, -1, -1):
    print(f"{i}.{second_list[i]}")
    # not this is fully done yet 
    

def trap():
    print("You stepped on a trap, you lose 1 heart")
    pisteet -=5

    # this  will take  a heart away from the player  since  each heart is worth 5 points


def  climate():
     pass

