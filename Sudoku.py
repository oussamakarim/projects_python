import pprint

def solve(board):
	find = empty_box(board)
	if find:
		row, col = find
	else:
		return True

	for i in range(1,10):
		if valid(board,(row, col), i):
			board[row][col]=i

			if solve(board):
				return True

			board[row][col]=0

	return False

def valid(board, position, num):

	#check Row
	for i in range(0, len(board)):
		if board[position[0]][i] == num and position[1] != i:
			return False
	#check Col
	for i in range(0,len(board)):
		if board[i][position[1]] == num and position[1] != i:
			return False

	# Check Box
	box_x = position[1]//3
	box_y = position[0]//3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if board[i][j] == num and (i,j) != position:
				return False

	return True

def empty_box(board):
	for i in range(len(board)):
		for j in range (len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None

def display_board(board):
	for i in range(len(board)):
		if i%3 == 0 and i !=0:
			print("--------------------")
		for j in range (len(board[0])):
			if j%3 == 0:
				print("|", end="")

			if j==8:
				print(board[i][j], end="\n")
			else:
				print(str(board[i][j]) + " ", end="")

board = [
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
]

solve(board)
display_board(board)