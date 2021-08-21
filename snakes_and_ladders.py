import random
import copy

class SnakesAndLadders:
    """Single player snakes and ladder game"""

    def __init__(self):
        self.array_num=[]
        self.number_state = {
            4:"(+11)",
            13:"(+33)",
            27:"(-22)",
            33:"(+16)",
            40:"(-37)",
            42:"(+21)",
            43:"(-25)",
            50:"(+19)",
            54:"(-23)",
            62:"(+19)",
            66:"(-21)",
            74:"(+18)",
            76:"(-18)",
            89:"(-36)",
            99:"(-55)",
        }

    def create_map(self):
        self.array_num = []
        i = 1
        row_count = 1
        num=[]
        for j in range(100,0,-1):
            formatted_num = self.__assign_values(j)
            num.append(formatted_num)
            if i%10==0:
                if row_count % 2==0:
                    num.reverse()
                    self.array_num.append(num.copy())
                else:
                    self.array_num.append(num.copy())
                num.clear()
                row_count+=1
            i += 1

        self.display_map(self.array_num)

    def __assign_values(self,number):
        if number in self.number_state.keys():
            format= "{0}{1}".format(number,self.number_state[number])
        else:
            format = "{:2d}\t".format(number)
        return format

    def get_array_num(self):
        return self.array_num

    #display the map
    def display_map(self,arr_list):
        for i in arr_list:
            print(*i)

    #get the current number from the main list 
    def format_num(self, Player1):
        if Player1 % 10 == 0:
            index = (Player1 // 10) - 1
        else:
            index = Player1 // 10
        arr = self.get_array_num()   
        get_num = arr[9 - index]
        value = [data for data in get_num if str(Player1) in data][0].split('(')[0]
        return value

load = SnakesAndLadders()
load.create_map()
Player1=1
print("***** Player 1(P1) starts from 1 ******\n")
while True:
    dice_input =str(input("Type 't' to throw the dice: "))
    if dice_input.lower() == "t":
        dice_value = random.randint(1,6)
        Player1 += dice_value
        print("*****You threw {0} *******\n".format(dice_value))
        if Player1 == 100:
            print("Player 1 wins!!")
            break
        elif Player1 >100:
            Player1 -= dice_value
            print("You need {0} to win!!\n".format(100-Player1))
            continue
        message = None       
        value = load.format_num(Player1)
        int_value = int(value)
        if int_value in load.number_state.keys():
            num_state = load.number_state[int_value]
            if "+" in num_state:
                add = num_state[2:4]
                int_value += int(add)
                message = "***** You took a ladder from {0} to {1} *****\n".format(Player1,int_value)
            else:
                subtract = num_state[2:4]
                int_value -= int(subtract)
                message = "***** OOPS!!. The snake bit you. You dropped from {0} to {1} *****\n".format(Player1,int_value)


        Player1 = int_value
        if int(value) != Player1:
            value = load.format_num(Player1)

        temp = copy.deepcopy(load.get_array_num())

        for i in temp:
            for n,j in enumerate(i):
                if "(" in j:
                    t = j.split('(')[0]
                else:
                    t = j
                if value == t:                    
                    i[n] = "P1=" + j

        if message is not None:
            print(message)

        load.display_map(temp)
    else:
        print("C'mon buddy. Please type t")