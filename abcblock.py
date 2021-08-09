import random
import re 

class Input_Processor:
    def __init__(self) -> None:
        pass
    def Input_check(self):
        while(True):
            inputtext = input("input : ")
            if (type(inputtext) == str and re.findall("^[a-kA-K]$",inputtext)):
                return inputtext.upper()
            else:
                print("Input invalid")
class abcblocks:
    def __init__(self):
        self.Board_array = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
    def random_map(self):
        charslist = ['A','B','C','D','E','F','G','H','I','J','K']
        count = 0
        while len(charslist) > 0:
            rand = int(random.random() * (len(charslist)))
            self.Board_array[count // 4][count % 4] = charslist.pop(rand)
            count += 1
    def checkwin(self):
        return self.Board_array == [["A","B","C","D"], ["E","F","G","H"], ["I","J","K"," "]]
    def move(self, cha):
        y = 0
        x = 0
        for checky in range(3):
            for checkx in range(4):
                if (self.Board_array[checky][checkx] == cha):
                    y = checky
                    x = checkx
                    break
        if y-1 >= 0 and y-1 <= 2:
            if (self.Board_array[y-1][x] == " "):
                self.Board_array[y-1][x],self.Board_array[y][x] = self.Board_array[y][x],self.Board_array[y-1][x]
                return True
        if y+1 >= 0 and y+1 <= 2:
            if (self.Board_array[y+1][x] == " "):
                self.Board_array[y+1][x],self.Board_array[y][x] = self.Board_array[y][x],self.Board_array[y+1][x]
                return True
        if x-1 >= 0 and x-1 <= 3:
            if (self.Board_array[y][x-1] == " "):
                self.Board_array[y][x-1],self.Board_array[y][x] = self.Board_array[y][x],self.Board_array[y][x-1]
                return True
        if x+1 >= 0 and x+1 <= 3:
            if (self.Board_array[y][x+1] == " "):
                self.Board_array[y][x+1],self.Board_array[y][x] = self.Board_array[y][x],self.Board_array[y][x+1]
                return True
        print("Invalid Move")
        return False
    def display_board(self):
        print(f" {self.Board_array[0][0]} | {self.Board_array[0][1]} | {self.Board_array[0][2]} | {self.Board_array[0][3]} ")
        print(f"---------------")
        print(f" {self.Board_array[1][0]} | {self.Board_array[1][1]} | {self.Board_array[1][2]} | {self.Board_array[1][3]} ")
        print(f"---------------")
        print(f" {self.Board_array[2][0]} | {self.Board_array[2][1]} | {self.Board_array[2][2]} | {self.Board_array[2][3]} ")
        print()


A = Input_Processor()
game = abcblocks()
game.random_map()
game.display_board()
while(not game.checkwin()):
    while(not game.move(A.Input_check())):
        pass
    game.display_board()
