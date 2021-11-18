def displayGame(gameList):
  print("Here is the current list:")
  print(gameList)
  
def positionChoice():
  choice = "wrong"
  
  while choice not in ["0", "1", "2"]:
    
    choice = input("Pick a position (0, 1 or 2): ")
    
    if choice not in ["0", "1", "2"]:
      print("Invalid choice")
      
  return int(choice)
  
def replacementChoice(gameList, position):
  userPlacement = input("Type a string to palce at position: ")
  
  gameList[position] = userPlacement
  
  return gameList

positionChoice()