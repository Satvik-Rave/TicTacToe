board=["-","-","-",
       "-","-","-",
       "-","-","-",]
game_running = True
winner = None
cur_player = "X"

def disp_board():
       print(board[0] + "|" + board[1] + "|" + board[2])
       print(board[3] + "|" + board[4] + "|" + board[5])
       print(board[6] + "|" + board[7] + "|" + board[8])

def play_ttt():

       disp_board()

       while game_running:
              handle_turn(cur_player)
              game_over()
              flip_player_turn()

       if winner == "X" or winner == "O":
              print (winner + " won.")
       elif winner == None:
              print ("It's a tie.")

def handle_turn(player):
       print(player , "'s turn")
       place = input("Choose the position to mark(1-9):")

       valid = False
       while not valid:
              while place not in [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" ]:
                     place = input("INVALID CHOICE.Choose the position to mark again!!(1-9):")
              place = int(place) - 1

              if board[place] == "-":
                     valid = True
              else:
                     print("WRONG PLACE.TRY AGAIN!!")
       board[place] = player
       disp_board()

def game_over():
       game_won()
       game_tie()
       return

def game_won():
       global winner
       a = row_check()
       b = column_check()
       c = diagonals_check()
       if a:
              winner = a
       elif b:
              winner = b
       elif c:
              winner = c
       else:
              winner = None
       return

def row_check():
       global game_running
       row1 = board[0] == board[1] == board[2] != "-"
       row2 = board[3] == board[4] == board[5] != "-"
       row3 = board[6] == board[7] == board[8] != "-"
       if row1 or row2 or row3:
              game_running = False
       if row1:
              return board[0]
       elif row2:
              return board[3]
       elif row3:
              return board[6]
       return

def column_check():
       global game_running
       column1 = board[0] == board[3] == board[6] != "-"
       column2 = board[1] == board[4] == board[7] != "-"
       column3 = board[2] == board[5] == board[8] != "-"
       if column1 or column2 or column3:
              game_running = False
       if column1:
              return board[0]
       elif column2:
              return board[1]
       elif column3:
              return board[2]
       return

def diagonals_check():
       global game_running
       diagonal1 = board[0] == board[4] == board[8] != "-"
       diagonal2 = board[2] == board[4] == board[6] != "-"
       if diagonal1 or diagonal2:
              game_running = False
       if diagonal1:
              return board[0]
       elif diagonal2:
              return board[2]
       return

def game_tie():
       global game_running
       if "-" not in board:
              game_running = False

       return

def flip_player_turn():
       global cur_player
       if cur_player == "X":
              cur_player = "O"
       elif cur_player == "O":
              cur_player = "X"
       return

play_ttt()

