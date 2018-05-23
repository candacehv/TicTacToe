class Board:
    square1 = ["|_","_"," |"]
    square2 = ["_","_"," |"]
    square3 = ["_","_","_|"]
    square4 = ["|_","_"," |"]
    square5 = ["_","_"," |"]
    square6 = ["_","_","_|"]
    square7 = ["|_","_"," |"]
    square8 = ["_","_"," |"]
    square9 = ["_","_","_|"]

    str1 = "".join(square1)
    str2 = "".join(square2)
    str3 = "".join(square3)
    str4 = "".join(square4)
    str5 = "".join(square5)
    str6 = "".join(square6)
    str7 = "".join(square7)
    str8 = "".join(square8)
    str9 = "".join(square9)

    counter = 1


def update_board(location, player):
    if location == 1:
        if Board.square1[1] == "_":
            if player == 1:
                Board.square1[1] = "X"
            else:
                Board.square1[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)
            
    if location == 2:
        if Board.square2[1]== "_":
            if player == 1:
                Board.square2[1] = "X"
            else: 
                Board.square2[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)                
    if location == 3:
        if Board.square3[1]== "_":
            if player == 1:
                Board.square3[1] = "X"
            else:
                Board.square3[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   
    if location == 4:
        if Board.square4[1]== "_":
            if player == 1:
                Board.square4[1] = "X"
            else:
                Board.square4[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   
    if location == 5:
        if Board.square5[1]=="_":
            if player == 1:
                Board.square5[1] = "X"
            else:
                Board.square5[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   
    if location == 6:
        if Board.square6[1]=="_":
            if player == 1:
                Board.square6[1] = "X"
            else:
                Board.square6[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   
    if location == 7:
        if Board.square7[1]=="_":
            if player == 1:
                Board.square7[1] = "X"
            else:
                Board.square7[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   
    if location == 8:
        if Board.square8[1]=="_":
            if player == 1:
                Board.square8[1] = "X"
            else:
                Board.square8[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   
    if location == 9:
        if Board.square9[1]=="_":
            if player == 1:
                Board.square9[1] = "X"
            else:
                Board.square9[1] = "O"
        else:
            location = input("That space is already taken. Please choose another:")
            update_board(location, player)   

    Board.str1 = "".join(Board.square1)
    Board.str2 = "".join(Board.square2)
    Board.str3 = "".join(Board.square3)
    Board.str4 = "".join(Board.square4)
    Board.str5 = "".join(Board.square5)
    Board.str6 = "".join(Board.square6)
    Board.str7 = "".join(Board.square7)
    Board.str8 = "".join(Board.square8)
    Board.str9 = "".join(Board.square9)


    display_board()

    check_for_winner(location)

def check_for_winner(location):
    if location == 1:
        if (Board.str1[2]==Board.str2[1] and Board.str1[2]==Board.str3[1]) or (Board.str1[2]==Board.str4[2] and Board.str1[2]==Board.str7[2]) or (Board.str1[2]==Board.str5[1] and Board.str1[2]==Board.str9[1]):
            if Board.str1[2] == "X":
                print "Player 1 Wins!"
                
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
           print "It's a tie! Everyone wins, yayyy! :)"
           play_again()
        else:
            player_turn()
    if location == 2:
        if (Board.str2[1]==Board.str5[1] and Board.str2[1]==Board.str8[1]) or (Board.str2[1]==Board.str1[2] and Board.str2[1]==Board.str3[1]):
            if Board.str2[1] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()
    if location == 3:
        if (Board.str3[1]==Board.str2[1] and Board.str3[1]==Board.str1[2]) or (Board.str3[1]==Board.str6[1] and Board.str3[1]==Board.str9[1]) or (Board.str3[1]==Board.str5[1] and Board.str3[1]==Board.str7[2]):
            if Board.str3[1] == "X":
                print "Player 1 Wins!"
                play_again()
            else:
                print "Player 2 Wins!"
            play_again()
            
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
            start_again()
        else:
            player_turn()
    if location == 4:
        if (Board.str4[2]==Board.str5[1] and Board.str4[2]==Board.str6[1]) or (Board.str4[2]==Board.str1[2] and Board.str4[2]==Board.str7[2]):
            if Board.str4[2] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()
    if location == 5:
        if (Board.str5[1]==Board.str2[1] and Board.str5[1]==Board.str8[1]) or (Board.str5[1]==Board.str4[2] and Board.str5[1]==Board.str6[1]) or (Board.str5[1]==Board.str1[2] and Board.str5[1]==Board.str9[1]) or (Board.str5[1]==Board.str3[1] and Board.str5[1]==Board.str7[2]):
            if Board.str5[1] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()
    if location == 6:
        if (Board.str6[1]==Board.str5[1] and Board.str6[1]==Board.str4[2]) or (Board.str6[1]==Board.str3[1] and Board.str6[1]==Board.str9[1]):
            if Board.str6[1] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10: 
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()
    if location == 7:
        if (Board.str7[2]==Board.str1[2] and Board.str7[2]==Board.str4[2]) or (Board.str7[2]==Board.str8[1] and Board.str7[2]==Board.str9[1]) or (Board.str7[2]==Board.str5[1] and Board.str7[2]==Board.str3[1]):
            if Board.str7[2] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()
    if location == 8:
        if (Board.str8[1]==Board.str7[2] and Board.str8[1]==Board.str9[1]) or (Board.str8[1]==Board.str5[1] and Board.str8[1]==Board.str2[1]):
            if Board.str8[1] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()
    if location == 9:
        if (Board.str9[1]==Board.str8[1] and Board.str9[1]==Board.str7[2]) or (Board.str9[1]==Board.str6[1] and Board.str9[1]==Board.str3[1]) or (Board.str9[1]==Board.str5[1] and Board.str9[1]==Board.str1[2]):
            if Board.str9[1] == "X":
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
            play_again()
        elif Board.counter==10:
            print "It's a tie! Everyone wins, yayyy! :)"
            play_again()
        else:
            player_turn()        

def player_turn():
    player = 1
    if Board.counter%2 == 0:
        player = 2
        print "Player 2"
        Board.counter += 1
    else:
        player = 1
        print "Player 1"
        Board.counter += 1
    update_board(new_move(), player)


def new_move():
    move = input("Choose a square:")
    return move
        
def display_board():
    print Board.str1 + Board.str2 + Board.str3
    print Board.str4 + Board.str5 + Board.str6    
    print Board.str7 + Board.str8 + Board.str9

def play_again():
    if raw_input("Do you want to play again? (Y/N)").lower() == "y":
        clear_board()
        display_board()
        player_turn()


def clear_board():

    Board.counter = 1
    Board.square1 = ["|_","_"," |"]
    Board.square2 = ["_","_"," |"]
    Board.square3 = ["_","_","_|"]
    Board.square4 = ["|_","_"," |"]
    Board.square5 = ["_","_"," |"]
    Board.square6 = ["_","_","_|"]
    Board.square7 = ["|_","_"," |"]
    Board.square8 = ["_","_"," |"]
    Board.square9 = ["_","_","_|"]

    Board.str1 = "".join(Board.square1)
    Board.str2 = "".join(Board.square2)
    Board.str3 = "".join(Board.square3)
    Board.str4 = "".join(Board.square4)
    Board.str5 = "".join(Board.square5)
    Board.str6 = "".join(Board.square6)
    Board.str7 = "".join(Board.square7)
    Board.str8 = "".join(Board.square8)
    Board.str9 = "".join(Board.square9)

    
##Begin game here, original state
display_board()

##Defines player whose turn it is and calls new_move(player)
##and update_board(new_move(player), player)
player_turn()

