"""
Ubayd Abdul Majit
UPI: uabd315
ID: 765724280
Purpose: My program plays Connect Four - align 4 'o' in any direction to score points
Note: To change size of gameboard, go to 'display_entry()' function, inside while loop, stored in 'game' var. By default, size = 6.
Made in VSCode - Does not run on Py IDLE
"""

user_entry = [] # user list appends user entry - later displayed in leaderboard
#Colours
CBLUE = '\33[94m'
CRED = '\33[31m'
CEND = '\033[0m'
CUNDER = '\33[21m'

def display_entry():
    #Display start up page to start game
    print("___________________Connect Four___________________")
    print("|               Ubayd Abdul Majit                |")
    print("|                                                |")
    print("|                  How to play                   |")
    print("|                  -----------                   |")
    print("|            Player is 'o' & AI is 'x'           |")
    print("|           To win points, connect 4 'o'         |")
    print("|        Game ends when all columns are full     |")
    print("|                  -----------                   |")
    print("|                   Goodluck!                    |")
    print("|       ↘️ To start type ur (alias) name↙️         |")
    user_inp =input("                   Type here:").capitalize()

    #user validation
    while len(user_inp) > 0:
        if len(user_inp) > 1 and len(user_inp) < 10:
            user_entry.append(user_inp) 
            game = FourInARow(6)
            game.play()
            break
        else:
            user_inp =input("Name must be an alphabet, be greater than 1 char & less than 10. Enter: ").capitalize()
    quit()

class GameBoard:
    def __init__(self, size):
        self.size=size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2
    
    def num_free_positions_in_column(self, column):
        return self.size if self.num_entries[column] == 0 else (self.size - self.num_entries[column])
    
    def game_over(self):
        for i in range(self.size):
            if self.num_entries[i] != self.size:
                return False   
        return True
    
    def display(self):
        # Displays board
        print("_________________________________")
        print(CBLUE+f"Points: P1 {user_entry[-1]}: {self.points[0]}"+CEND)
        print(CRED+f"Points: P2  AI: {self.points[1]}"+CEND)
        print("---------------------------------")
        for i in range(self.size):
            for x in self.items:
                x = x[::-1]
                if x[i] == 0:
                    print(" ", end=" ")
                elif x[i] == 1:
                    print(CBLUE+"o"+CEND, end=" ")
                elif x[i] == 2:
                    print(CRED+"x"+CEND, end = " ")
            print()
        print('-' * (2*self.size-1))
        print(' '.join(map(str, range(self.size))))
    
    def add(self, column, player): 
        if self.num_entries[column] >= self.size or column >= self.size:
            return False
        else:
            # add disc
            if self.num_free_positions_in_column(column) != 0:
                row_number = self.items[column].index(0)
            self.items[column][row_number] = player
            self.num_entries[column] += 1
            self.points[player-1] += self.num_new_points(column,row_number,player)
            return True
     
    def num_new_points(self, column, row, player):
        # total number of points scored by player
        return (self.horizontal_points_check(column, row, player)+self.vertical_points_check(column, row, player)+self.diagonal_points_check(column, row, player)+self.diagonal_reversed_points_check(column, row, player))
        
    def horizontal_points_check(self, column, row, player):
        # Horizontal check for 4 discs in a sequence 
        horizontal = 0
        for i in range(column-3, column+1):
            if i >= 0:
                try:
                    if self.items[i][row] == player and self.items[i+1][row] == player and self.items[i+2][row] == player and self.items[i+3][row] == player:
                        horizontal += 1
                except:
                    continue
        return horizontal

    def vertical_points_check(self, column, row, player):
        # Vertical check for 4 discs in a sequence 
        vertical = 0
        for i in range(row-3, row+1):
            if i >= 0:
                try:
                    if self.items[column][i] == player and self.items[column][i+1] == player and self.items[column][i+2] == player and self.items[column][i+3] == player:
                        vertical += 1
                except:
                    continue
        return vertical

    def diagonal_points_check(self, column, row, player):
        # Diagonal check for 4 discs in a sequence 
        diagonal = 0
        for i in range(-3, 1):
            if column+i >= 0 and row+i >= 0:
                try:
                    if self.items[column+i][row+i] == player and self.items[column+i+1][row+i+1] == player and self.items[column+i+2][row+i+2] == player and self.items[column+i+3][row+i+3] == player:
                        diagonal += 1
                except:
                    continue
        return diagonal

    def diagonal_reversed_points_check(self, column, row, player):
        # Diagonal reversed check for 4 discs in a sequence 
        diagonal_rev = 0
        for i in range(-3, 1):
            if column+i >= 0 and row-i-3 >= 0:
                try:
                    if self.items[column+i][row-i] == player and self.items[column+i+1][row-i-1] == player and self.items[column+i+2][row-i-2] == player and self.items[column+i+3][row-i-3] == player:
                        diagonal_rev += 1
                except:
                    continue
        return diagonal_rev

    def free_slots_as_close_to_middle_as_possible(self):
        empty_list = []
        if self.size % 2 == 0:
            # even case
            mid_even = self.size//2
            for i in range(mid_even):
                empty_list.append((self.size-1)//2 - i) 
                empty_list.append((self.size-1)//2 + i + 1)
        else:
            # odd case
            mid_odd = (self.size-1)//2
            empty_list.append(mid_odd)
            for i in range(1,mid_odd+1):
                empty_list.append(mid_odd - i) 
                empty_list.append(mid_odd + i)
        for x in range(len(empty_list)-1,-1,-1):
            if self.num_free_positions_in_column(empty_list[x]) == 0: empty_list.pop(x)
                
        return empty_list
    
    def column_resulting_in_max_points(self, player):
        mid_close = self.free_slots_as_close_to_middle_as_possible()
        max_points = self.store_max_points(player)
        if len(mid_close) > 0:
            for i in range(len(mid_close)):
                for x in range(len(max_points)):
                    #check same as player
                    if mid_close[i] == max_points[x][0]:
                        return tuple(max_points[x])
        else:
            return tuple([])

    def add_player_to_free_slots(self, player):
        # finds free slot and adds disc
        add_list = []
        offset = -1
        for i in range(self.size):
            curr = self.points[player-1]
            if self.num_free_positions_in_column(i) != 0:
                offset = self.items[i].index(0)
                self.add(i, player)
                reg = self.points[player-1] - curr
                add_list.append([i, reg])
                self.items[i][offset] = 0
                self.num_entries[i] -= 1
                self.points[player-1] = curr
        return add_list

    def store_max_points(self, player):
        # find which column results in max points
        add_points = self.add_player_to_free_slots(player) 
        max_points = []
        offset = 0
        for i in range(len(add_points)):
            if add_points[i][1] > offset:
                offset = add_points[i][1]
        for x in range(len(add_points)):
            if add_points[x][1] == offset:
                max_points.append(add_points[x])
        return max_points

class FourInARow:
    def __init__(self, size):
        self.board=GameBoard(size)
    
    def play(self):
        print("\n***************|  NEW GAME  |***************")
        self.board.display()
        player_number=0
        print()
        while not self.board.game_over():
            if player_number+1 == 1:
                #print user name
                print("P",player_number+1,f"{user_entry[-1]}:")
            elif player_number+1 == 2:
                print("P",player_number+1,f"AI:")
            if player_number==0:
                valid_input = False
                while not valid_input:
                    try:
                        column = int(input("Please input slot: "))       
                    except ValueError:
                        print("Input must be an integer in the range 0 to ", self.board.size-1)
                    else:
                        if column<0 or column>=self.board.size:
                            print("Input must be an integer in the range 0 to ", self.board.size-1)
                        else:
                            if self.board.add(column, player_number+1):
                                valid_input = True
                            else:
                                print("Column ", column, "is already full. Please choose another one.")
            else:
                # Choose move which maximises new points for computer player
                (best_column, max_points)=self.board.column_resulting_in_max_points(2)
                if max_points>0:
                    column=best_column
                else:
                    # if no move adds new points choose move which minimises points opponent player gets
                    (best_column, max_points)=self.board.column_resulting_in_max_points(1)
                    if max_points>0:
                        column=best_column
                    else:
                        # if no opponent move creates new points then choose column as close to middle as possible
                        column = self.board.free_slots_as_close_to_middle_as_possible()[0]
                self.board.add(column, player_number+1)
                print("The AI chooses column ", column)
            self.board.display()   
            player_number=(player_number+1)%2
        if (self.board.points[0]>self.board.points[1]):
            print(CBLUE+f"{user_entry[-1]} (circles 'o') wins!"+CEND)
            self.leaderboard()
        elif (self.board.points[0]<self.board.points[1]):    
            print(CRED+"AI (crosses 'x') wins!"+CEND)
            self.leaderboard()
        else:  
            print("It's a draw!")
            self.leaderboard()

    def leaderboard(self):
        """ prints leaderboard of users max points at end of game """
        #Opens file to save user name and points
        name = user_entry[0]
        file = open("leaderBoard.txt", "a") #insert the leader file in here.
        curr = user_entry[-1]

        if name == "admin":
            file = open("leaderBoard.txt", "w")
        else:
            file.write(str(self.board.points[0])) #mention score along with user name inputted by the user.
            file.write(" - ")
            file.write(name + "\n") 
            file.close()
        
        inputFile = open("leaderBoard.txt", 'r')
        lineList = inputFile.readlines()
        lineList.sort()
        
        highest = [] #highest 10 scores saved in this list
        highest_20 = (lineList[-20:])#top 20 highest scores will be displayed.
        for line in highest_20:
            point = line.split(" - ") #format each line.
            highest.append((int(point[0]), point[1]))
        file.close()
        highest.sort(); highest.reverse()

        # Display Leaderboard
        return_string = ""
        for i in range(len(highest)): 
            if highest[i][1]== curr+"\n":
                #return current users as coloured
                return_string += CBLUE+"{} - {}".format(highest[i][0], highest[i][1])+CEND
            else:
                return_string += "{} - {}".format(highest[i][0], highest[i][1])
        print()
        print(CUNDER+"_______Top10 LEADERBOARD_______"+CEND)
        print("\t Score - Name")
        print(CBLUE+f"\t Your score: {self.board.points[0]}"+CEND)
        print("-------------------------------")
        print(return_string)
       
# MAIN
display_entry()          

