import random
import os

potion = False

def aarin_vastaus():
    global potion
    
    treasure = random.randint(1,5)
   
    if treasure == 4:
        print("u got a bonus heart")

        if potion == True:
            print("since the potion is active u get 2x effect from the treasure")
            potion = False 
        heart()
   
    elif treasure == 3:
        print("Trap activated, you lose 1 heart")
        if potion == True:
            print("since the potion is active u get 2x effect from the treasure")
            potion = False
        trap()
      
    elif treasure == 1:
        print("You potion next chess will give u 2x")
        doublex()

    elif treasure == 2: 
        print("You Found a Empty chest, better luck next time")
    elif treasure == 5:
        print("You Found a Empty chest, better luck next time")

    else:
        print("You Found a Empty chest, better luck next time")


def aarin_avaus_kysymys():
    
    from art import chess1  
    from art import openchess1
    import main2
    chess1()
    print("Hei, onneksi olkoon, löysit aarteen, haluatko avata sen? kyllä/ei")
    vastaus = str(input()).lower()
    if vastaus == "kyllä":
        openchess1()
        aarin_vastaus()
    elif vastaus == "ei":
        print("okei, jatketaan matkaa")
        os.system('cls')
    else:
        print("Vastaa vain kyllä tai ei")
    
def doublex():
    global potion
    potion = True
    print("Onneksi olkoon! Taikajuoma on aktivoitu! saat 2x vaikutuksen seuraavasta aarteesta")

def trap():
   
    pisteet -= 5
    print("Look out! You fell into a trap, you lose 5 points")
def  heart():
    pisteet += 5
    print("You found a heart, you gain 5 points")
