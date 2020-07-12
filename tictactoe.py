from random import randrange

list1 = [[i+1+j*3 for i in range(3)] for j in range(3)]
def DisplayBoard(board):
	incr = 0
	print("+-----+-----+-----+") 
	for col in range(3):
		for row in range(3):
			print ("|",list1[col][row], sep="  ",end="  ")
		incr += row
		print("|")
		print("+-----+-----+-----+") 
def VictoryFor (board,sign):
	won = 0
	for i in range (3):
		if (board [i][i] == sign):
			won += 1
		if (won == 3):
			return False
	won = 0
	for i in range (2,-1):
		if (board [i][i] == sign):
			won += 1
		if (won == 3):
			return False
	
	for i in range (3):
		if (board [i][0] == sign and board [i][1] == sign and board [i][2] == sign):
			return False
		if (board [0][i] == sign and board [1][i] == sign and board [2][i] == sign):
			return False
	return True
def CheckPos (board, usr_move, sign,chk_full):
	if (usr_move in (1,2,3)):
		row_pos = 0
		col_pos = usr_move-1
	elif (usr_move in (4,5,6)):
		row_pos = 1
		col_pos = usr_move - 4
	elif (usr_move in (7,8,9)):
		row_pos = 2
		col_pos = usr_move - 7
	if (board[row_pos][col_pos] == 'O' or board[row_pos][col_pos] == 'X'):
		return True
	else:
		if (not chk_full):
			board[row_pos][col_pos] = sign
		return False
def CheckDraw(board):
	filled = 0
	for i in range(1,10):
		if (CheckPos (board, i, "O", True) or CheckPos (board, i, "X", True)):
			filled += 1
	if (filled == 9):
		DisplayBoard(board)
		print ("Its a draw, you can restart the game !")
		return True
	else:
		return False
	
won = True
comp_move = 5
while (won):
	DisplayBoard(list1)
	print ("Its computer move now.....");
	while (CheckPos (list1,comp_move, "X", False)):
		comp_move = randrange(9)+1
	DisplayBoard(list1)
	won = VictoryFor (list1, "X");
	if (not won):
		DisplayBoard(list1)
		print ("Computer Won, you lost !!!")
		break;
	else:
		if (not CheckDraw(list1)):	
			usr_move = int(input("Enter your move or position: "))
			while (usr_move not in range(1,10) or CheckPos (list1, usr_move,"O", False)):
				usr_move = int(input("Position occupied or not correct, re-enter your move or position: "))
			won = VictoryFor (list1,"O");
			if (not won):
				DisplayBoard(list1)
				print ("You've won! Hurray! ")
				break;
		else:
			break;
		if (CheckDraw(list1)):
			break;
