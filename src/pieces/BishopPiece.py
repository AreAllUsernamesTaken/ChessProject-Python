from ChessPiece import ChessPiece

class Bishop(ChessPiece):
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		# The Bishop can not move paralel with the OX axis
		if yCoordinate == newY:
			return False

		# The Bishop movement is paralel with either of the main diagonals
		slope = (xCoordinate - newX) / (yCoordinate - newY)
		if slope != 1 and slope  != -1:
			return False
		return True

	def collision_check(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		slope = (xCoordinate - newX) / (yCoordinate - newY)
		high_x = min(xCoordinate, newX)
		low_x = max(xCoordinate, newX)
		# Movement along main diagonal means (X - Y) is constant. 
		if slope == 1:
			for i in range(high_x + 1, low_x):
					if not board[i][abs(xCoordinate - yCoordinate) + i] is None:
						return True
		
		# Movement along secondary diagonal means (X + Y) is constant.
		if slope == -1:
			for i in range(high_x + 1, low_x):
					if not board[i][xCoordinate + yCoordinate - i] is None:
						return True
		return False


	def print(self) -> str:
		return " ♝ "