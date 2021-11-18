from IPython.core.display import display
from IPython.display import clear_output

def displayBoard(board):
  clear_output()
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('-----')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-----')
  print(board[7] + '|' + board[8] + '|' + board[9])

def assignMarkers():
  player1Marker = ''
  
  while player1Marker != 'X' and player1Marker != 'O':
    player1Marker = input('Player 1, choose X or O: ').upper()

  if player1Marker == 'X':
    player2Marker = 'O'
  else:
    player2Marker = 'X'
  
  return (player1Marker, player2Marker)

def playerPosition():
  position = ''
  
  while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    position = input("Enter a position to place your marker (1 - 9): ")
    
  return int(position)

def playerPosition2(takenPositions):
  validInput = False
  
  
  while validInput == False:
    position = input("Enter a position to place your marker (1 - 9): ")
    if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and position not in takenPositions:
      takenPositions.append(position)
      validInput = True
    elif position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      print('Please choose a number between 1 - 9')
    elif position in takenPositions:
      print('That position has already been taken')

  return int(position)

def placeMarker(board, marker, position):
  board[position] = marker

def switchPlayer(currentPlayer):
  if currentPlayer == 'X':
    currentPlayer = 'O'
  elif currentPlayer == 'O':
    currentPlayer = 'X'
    
  return currentPlayer

def winOrTie(board, marker):
  #Horizontal win:
  if board[1] == board[2] == board[3] == marker or board[4] == board[5] == board[6] == marker or board[7] == board[8] == board[9] == marker:
    return True
  #Vertical win:
  elif board[1] == board[4] == board[7] == marker or board[2] == board[5] == board[8] == marker or board[3] == board[6] == board[9] == marker:
    return True
  #Diagonal win
  elif board[1] == board[5] == board[9] == marker or board[3] == board[5] == board[7] == marker:
    return True

def game():
  player1Marker, player2Marker = assignMarkers()
  print(f'Player 1 is: {player1Marker}')
  print(f'Player 2 is: {player2Marker}')
  
  print('Below are the possible positions to place your marker')
  print('1' + '|' + '2' + '|' + '3')
  print('-----')
  print('4' + '|' + '5' + '|' + '6')
  print('-----')
  print('7' + '|' + '8' + '|' + '9') 
  
  takenPositions = []
  board = [' '] * 10
  print('\n')
  displayBoard(board)
  moves = 1
  currentPlayer = player1Marker
  while moves != 10:
    print(f'It\'s {currentPlayer}\'s turn')
    
    position = playerPosition2(takenPositions)
    
    placeMarker(board, currentPlayer, position)
    
    displayBoard(board)
    
    if winOrTie(board, currentPlayer) == True:
      print(f'{currentPlayer} wins!')
      break
    
    moves += 1
    currentPlayer = switchPlayer(currentPlayer)
  else:
    print("It's a tie!")
    
game()