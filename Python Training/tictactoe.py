gameOn = True
winner = None
correctSelection = False
computer = None

#BOARD CONTENT
board = [".", ".", "."
		, ".", ".", "."
		, ".", ".", "."]

availableSquares = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#CURRENT PLAYER
currentPlayer = "X"

#PRINT THE CURRENT BOARD
def printBoard():
	print("")
	print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
	print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
	print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
	print("")

#USER COMMAND
def userCommand(square):
	global currentPlayer
	global correctSelection
	global availableSquares
	inp = int(square) - 1
	if inp in availableSquares:
		correctSelection = True
		availableSquares.remove(inp)
		if currentPlayer == 'X':
			board[inp] = 'X'
			currentPlayer = 'O'
		elif currentPlayer == 'O':
			board[inp] = 'O'
			currentPlayer = 'X'
	else:
		print("\n --Not a correct square, try again-- \n")

#CHECK IF SOMEONE WON HORIZONTAL
def checkHorizontal():
	global winner
	if board[0] == board[1] == board[2] and board[0] != ".":
		winner = board[0]
	if board[3] == board[4] == board[5] and board[3] != ".":
		winner = board[3]
	if board[6] == board[7] == board[8] and board[6] != ".":
		winner = board[6]

#CHECK IF SOMEONE WON VERTICAL
def checkVertical():
	global winner
	if board[0] == board[3] == board[6] and board[0] != ".":
		winner = board[0]
	if board[1] == board[4] == board[7] and board[1] != ".":
		winner = board[1]
	if board[2] == board[5] == board[8] and board[2] != ".":
		winner = board[2]

#CHECK IF SOMEONE WON DIAGONAL
def checkDiagonal():
	global winner
	if board[0] == board[4] == board[8] and board[0] != ".":
		winner = board[0]
	if board[2] == board[4] == board[6] and board[2] != ".":
		winner = board[2]

#MAIN FUNCTION
def main():
	global winner
	global gameOn
	global correctSelection
	global computer
	userInput = None

	userInput = input("Computer (Y/N): ")
	if userInput == "Y":
		computer = True
	elif userInput == "N":
		computer = False

	printBoard()
	while gameOn:
		while correctSelection == False:
			if currentPlayer == "X":
				userInput = input("Player X (1~9): ")
			else:
				userInput = input("Player O (1~9): ")
			userCommand(userInput)
		correctSelection = False
		printBoard()
		checkHorizontal()
		checkVertical()
		checkDiagonal()
		if winner == "X" or winner == "O":
			print("WINNER IS ", winner, " !!")
			gameOn = False

#START GAME
if 1==1:
	main()