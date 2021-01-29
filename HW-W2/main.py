import random


class Player:

    def __init__(self,name,taketurn,price):
        self.name = name
        self.taketurn = taketurn
        self.price = price
    
class Die:

    def __init__(self):
        pass
    
    def roll(self):
        x =0
        x = random.randint(1,6)
        print('first roll = ' , x)
        y= random.randint(1,6)
        print('second roll = ' , y)
        return x+y

class board:
    def __init__(self):
        z=[]
        for i in range(40):
            z.append(i)
        self.square = z
    

class MGAME:
    rounds = 20
    number_of_player = 5
    p1 = Player("Player_1",1,0)
    p2 = Player("Player_2",1,0)
    p3 = Player("Player_3",1,0)
    p4 = Player("Player_4",1,0)
    p5 = Player("Player_5",1,0)
    p6 = Player("Player_6",1,0)
    p7 = Player("Player_7",1,0)
    p8 = Player("Player_8",1,0)
    max_player=[p1,p2,p3,p4,p5,p6,p7,p8]
    Players = []
    die = Die()
    board = board()

    for i in range(number_of_player):

        Players.append(max_player[i])
    
    
    print("GAME START")
    for i in range(rounds):
        for j in range(len(Players)):
            print(Players[j].name," current price = ",Players[j].price)
            print(Players[j].name,"Turn : ",Players[j].taketurn,"type D for die")
                       
            x = input() 
            dies = die.roll()
            Players[j].price = Players[j].price + dies
            Players[j].taketurn = Players[j].taketurn+1
            print(Players[j].name," got ",dies)
            print(Players[j].name," new price = ",Players[j].price)

            if Players[j].price >= 40 :
                break

            
        if Players[j].price >= 40 :
            print(Players[j].name," WIN AT TURN :" , Players[j].taketurn)
            break
                


game = MGAME()


