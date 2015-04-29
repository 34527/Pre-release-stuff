#Euan McElhoney

import pdb
BOARDDIMENSION = 8

                
def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  TypeOfGame = TypeOfGame.lower()[0]
                       
  while TypeOfGame != "y" and TypeOfGame != "n":
      print("please enter Y or N")
      TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
      TypeOfGame = TypeOfGame.lower()[0]
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("       _______________________")
    print("R",RankNo, end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("       _______________________")
  print()
  print("       F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  if ColourOfPiece == "W":
    if StartRank == BOARDDIMENSION -1:
      if StartFile == FinishFile:
        if abs(FinishRank - StartRank) == 2:
          CheckRedumMoveIsLegal = True
         
  else:
    if StartRank == 2:
      if StartFile == FinishFile:
        if abs(FinishRank - StartRank) == 2:
          CheckRedumMoveIsLegal = True
      
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal


def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1) or  abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) ==1:
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or  (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if StartRank >BOARDDIMENSION or StartRank <1 or StartFile >BOARDDIMENSION or StartFile <1 or FinishRank >BOARDDIMENSION or FinishRank <1 or FinishFile >BOARDDIMENSION or FinishFile <1:
    MoveIsLegal = False
  else:
    if (FinishFile == StartFile) and (FinishRank == StartRank):
      MoveIsLegal = False
    else:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    InitialseSampleBoard(Board)
  elif SampleGame == "N":
    InitialiseNewBoard(Board)

def InitialseSampleBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
        Board[1][2] = "BG"
        Board[1][4] = "BS"
        Board[1][8] = "WG"
        Board[2][1] = "WR"
        Board[3][1] = "WS"
        Board[3][2] = "BE"
        Board[3][8] = "BE"
        Board[6][8] = "BR"

def InitialiseNewBoard(Board):
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    
                    

def GetMove(Square,Print):
  length = 12345
  while length !=2 :
    try:
      Square = int(input("{0}".format(Print)))
      length = len(str(Square))
      if length!=2:
        print("Invalid input, please enter a file and a rank")
    except:
   
      print("Invalid input, please enter a file and a rank")
  return Square

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  print()
  
  Colour1, Type1 = GetPieceName(Board[StartRank][StartFile])
  Colour2,Type2=GetPieceName(Board[FinishRank][FinishFile])
  if Type2 != " ":
    if Type1 != " ":

      print("{0} {1} takes {2} {3}".format(Colour1, Type1,Colour2,Type2))

  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("White Redum has been promoted to Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("Black Redum has been promoted to Marzaz Pani")
  
    
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "


def ConfirmMove(StartSquare, FinishSquare):
  a= (str(StartSquare)[0])
  b=(str(StartSquare)[1])
  c=(str(FinishSquare)[0])
  d=(str(FinishSquare)[1])
  
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}".format(a,b,c,d))
  confirm = input("Confirm move: ")
  confirm = confirm.lower()[0]
  return confirm

      
def GetPieceName(Piece):
  pieces = ["R","S","M","G","N","E"]
  pieces_full=["Reddum","Sarrum","Marzaz Pani","Gisgirgir","Nabu","Etlu"]
  PieceType = " "
  count=0
  for each in pieces:
      count = count+1
      if Piece[1] == each:
          PieceType = pieces_full[count -1]
      
        

  if Piece[0] == "W":
    PieceColour = "White"
  else:
    PieceColour = "Black"
  
  return PieceColour,PieceType

def display_menu():
  print()
  print("Main Menu")
  print()
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game") 
  print("4. View high scores")
  print("5. Settings")
  print("6. Quit program")

def get_menu_selection():
  valid = False
  while valid == False:
    print()
    menu_selection = int(input("Please enter your menu choice: "))
    if 0< menu_selection <7 :
      valid = True
  return menu_selection

def make_selection(menu_selection,main_menu):
   for count in range(2):
      if menu_selection == 1:
         
          menu_selection= play_game("n")
      elif menu_selection == 2:
        pass
      elif menu_selection == 3:
        
        menu_selection = play_game("y")
      elif menu_selection == 4:
        pass
      elif menu_selection == 5:
        pass
      elif menu_selection == 6:
        save_high_scores(scores)
        print("Exiting Game...")
        main_menu = False
        return main_menu     

      else:
        main_menu = True
        return main_menu     
def option_menu():
  print()
  print("Options")
  print()
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender")

def option_choice(PlayAgain):
  valid = False
  while valid == False:
    option = int(input("Please enter your menu choice: "))
    if 0< option < 5:
      valid = True
    else:
      print("Invalid Input")

  if option == 1:
    pass
  elif option == 2:
    PlayAgain = "n"
    
  elif option == 3:
    print()
    print("Returning to game")
    print()
  elif option == 4:
    print()
    print("Surrendering...")
  
  return PlayAgain,str(option)

def save_high_scores(scores):
  with open("high_scores.txt", mode="w", encoding = "utf-8") as file:
    file.write(scores)
  

  
def play_game(SampleGame):
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        confirm = "n"
        while confirm != "y":
          StartSquare = GetMove(StartSquare,"Enter coordinates of square containing piece to move (file first) or type '-1' for menu: ")
          if StartSquare == -1:
            option_menu()
            PlayAgain,option = option_choice(PlayAgain)
            if PlayAgain == "n":
              confirm = "y"
              MoveIsLegal = True
              GameOver = True
              menu_selection = None
            if option == "4":
              if WhoseTurn== "W":
                print()
                print("White surrenders, Black wins!")
                print()
                confirm = "y"
                MoveIsLegal = True
                GameOver = True
                menu_selection = None
              else:
                print()
                print("Black surrenders, White wins!")
                print()
                confirm = "y"
                MoveIsLegal = True
                GameOver = True
                menu_selection = None
            
              
          FinishSquare = 12345
          if StartSquare != -1:
            FinishSquare = GetMove(FinishSquare,"Enter coordinates of square to move piece to (file first) or type '-1' for menu:  ")
          if FinishSquare == -1:
            option_menu()
            PlayAgain,option = option_choice(PlayAgain)
            if PlayAgain == "n":
              confirm = "y"
              MoveIsLegal = True
              GameOver = True
              menu_selection = None

            if option == "4":
              if WhoseTurn== "W":
                print()
                print("White surrenders, Black wins!")
                print()
                confirm = "y"
                MoveIsLegal = True
                GameOver = True
                menu_selection = None
            else:
              print()
              print("Black surrenders, White wins!")
              print()
              confirm = "y"
              MoveIsLegal = True
              GameOver = True
              menu_selection = None
               
          StartRank = StartSquare % 10
          StartFile = StartSquare // 10
          FinishRank = FinishSquare % 10
          FinishFile = FinishSquare // 10
          if PlayAgain == "Y":
            MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")

          if StartSquare != -1 and FinishSquare != -1 and MoveIsLegal != False: 
            confirm = ConfirmMove(StartSquare,FinishSquare)


        if PlayAgain == "Y":
          GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
          MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)

      

          if GameOver:
            DisplayWinner(WhoseTurn)
            get_menu_selection()
            menu_selection = 123

          if WhoseTurn == "W":
            WhoseTurn = "B"
          else:
            WhoseTurn = "W"
        
  return menu_selection

if __name__ == "__main__":
  main_menu = True
  while main_menu == True:
    display_menu()
    menu_selection = get_menu_selection()
    main_menu = make_selection(menu_selection,main_menu)
