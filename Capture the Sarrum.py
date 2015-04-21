#https://github.com/longroadcomputing/COMP1-2015

# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment
# Victor Hugo Bahman

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
  Check = False
  while Check == False:
    TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
    TypeOfGame = TypeOfGame.upper()[0]
    if TypeOfGame != "Y" or TypeOfGame != "N":
      print("Please enter Y/N")
    else:
      Check = True
    
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
    print("{0}{1}".format(" "*5,"-"*25))
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("{0}{1}".format(" "*5,"-"*25))
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
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
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank): #stops pieces not moving
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1] #gets the type
    PieceColour = Board[StartRank][StartFile][0] #gets the colour

      
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False #stops blacks moving on white turn
      elif FinishRank < 1:
        MoveIsLegal = False
      elif FinishFile < 1:
        MoveIsLegal = False
      try:
        if Board[FinishRank][FinishFile][0] == "W": #stops landing on other pieces
          MoveIsLegal = False
      except IndexError: #stops going over 8
        MoveIsLegal = False

    else:
      if PieceColour != "B":
        MoveIsLegal = False #stops whites moving on black turn
      elif FinishRank < 1:
        MoveIsLegal = False
      elif FinishFile < 1:
        MoveIsLegal = False
      try:
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      except IndexError: #stops going over 8
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
  else:
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
                    
def GetMove(StartSquare, FinishSquare):
  Check = False
  Check2 = False
  while Check == False:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if len(str(StartSquare)) < 2 or len(str(StartSquare)) > 2:
          print("Please provide a file and a rank for this move")
      else:
          Check = True
    except ValueError:
      print("Please provide a file and a rank for this move")
      
  while Check2 == False:
    try:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if len(str(FinishSquare)) < 2 or len(str(FinishSquare)) > 2:
          print("Please provide a file and a rank for this move")
      else:
        Check2 = True
    except ValueError:
      print("Please provide a file and a rank for this move")
  return StartSquare, FinishSquare

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("White redum promoted to Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("Black redum promoted to Marzaz Pani")
  else:
    if Board[FinishRank][FinishFile] != "  ":
      FirstPiece = GetPieceName(StartRank,StartFile,Board)
      SecondPiece = GetPieceName(FinishRank,FinishFile,Board)
      print()
      print("{0} takes {1}".format(FirstPiece,SecondPiece)) 
      Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
      Board[StartRank][StartFile] = "  "
    else:
      Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
      Board[StartRank][StartFile] = "  "


def ConfirmMove(StartSquare,FinishSquare):
  StartSquare = str(StartSquare)
  FinishSquare = str(FinishSquare)
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartSquare[0],StartSquare[1],FinishSquare[0],FinishSquare[1]))
  Check = False
  while Check == False:
    ConfirmMove = input("Confirm move: ")
    ConfirmMove = ConfirmMove.upper()[0]
    if ConfirmMove != "Y" and ConfirmMove != "N":
      print("Please enter Y/N")
    else:
      Check = True
  if ConfirmMove == "Y":
    ConfirmMove = True
  else:
    ConfirmMove = False
  return ConfirmMove
    

def GetPieceName(Rank,File,Board):
  
  Piece = Board[Rank][File]
  if Piece == "BS":
    PieceName = "Black Sarrum"
  elif Piece == "BM":
    PieceName = "Black Marzaz Pani"
  elif Piece == "BN":
    PieceName = "Black Nabu"
  elif Piece == "BE":
    PieceName = "Black Etlu"
  elif Piece == "BG":
    PieceName = "Black Gisgigir"
  elif Piece == "BR":
    PieceName = "Black Redum"
  elif Piece == "WS":
    PieceName = "White Sarrum"
  elif Piece == "WM":
    PieceName = "White Marzaz Pani"
  elif Piece == "WN":
    PieceName = "WhiteNabu"
  elif Piece == "WE":
    PieceName = "White Etlu"
  elif Piece == "WG":
    PieceName = "White Gisgigir"
  else:
    PieceName = "White Redum"
  return PieceName

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
  print()

def get_menu_selection():
  Pass = False
  while Pass == False:
    Selection = input("Please select an option: ")
    try:
      if ord(Selection) < 49 or ord(Selection) > 54:
        print("That is not a valid option")
      else:
        Pass = True
    except TypeError:
      print("That is not a valid option")
  return Selection

def make_selection(Selection):
  SampleGame = None
  if Selection == 1:
    play_game()
  elif Selection == "2":
    load_game()
  elif Selection == "3":
    SampleGame = "Y"
  elif Selection == "4":
    pass
  elif Selection == "5":
    pass
  elif Selection == "6":
    quit()
  if SampleGame == None:
    SampleGame = "0"
  return Selection,SampleGame

  
def play_game(Selection):
  if Selection != "Y":
    Selection == "N"
  return Selection
    
def save_game():
  pass


def load_game():
  pass

def display_options():
  print()
  print("Options")
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")

def get_options():
  pass
  OptionSelection = input("Please select an option: ")
  if Selection != "1" or Selection != "2" or Selection != "3":
    print("Please select from the menu")
    
  return OptionSelection
  
def select_options(OptionSelection):
  pass
  if OptionSelection == "1":
    save_game()
  elif OptionSelection == "2":
    pass
  



if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  display_menu()
  Selection = get_menu_selection()
  Selection,SampleGame = make_selection(Selection)
  WhoseTurn = "W"
  while PlayAgain == "Y":
    GameOver = False
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      Confirm = False
      while not(MoveIsLegal) or not(Confirm):
        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        Confirm = ConfirmMove(StartSquare,FinishSquare)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if GameOver:
          DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
          WhoseTurn = "B"
      else:
          WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
