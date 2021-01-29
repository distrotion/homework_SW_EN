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
        x = random.randint(0,6)
        print('first roll = ' , x)
        y= random.randint(0,6)
        print('second roll = ' , y)
        return x+y

class board:
    def __init__(self):
        z=[]
        for i in range(40):
            z.append(i)
        self.square = z
    

class MGAME:

    number_of_player = 2
    p1 = Player("Player_1",0,0)
    p2 = Player("Player_2",0,0)
    p3 = Player("Player_3",0,0)
    p4 = Player("Player_4",0,0)
    p5 = Player("Player_5",0,0)
    p6 = Player("Player_6",0,0)
    p7 = Player("Player_7",0,0)
    p8 = Player("Player_8",0,0)
    max_player=[p1,p2,p3,p4,p5,p6,p7,p8]
    Players = []
    turn = 0
    die = Die()
    board = board()

    for i in range(number_of_player):
        Players.append(max_player[i])
    

    def __init__(self):
        print("GAME START")
        print(Players)
        




game = MGAME()

#p1 = Player("Tong",0,0)
#p2 = Player("parin",0,0)
#ply = [p1,p2]

#print(ply[0].name,ply[0].taketurn)
#print(ply[1].name,ply[1].taketurn)
#r1 = Die()
#print(r1.roll())
#b = board()
#print(b.square)
