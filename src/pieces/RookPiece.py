from ChessPiece import ChessPiece

class Rook(ChessPiece):
	# The rook can only move paralel with the axis (x = a or y = a)
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		if xCoordinate == newX or yCoordinate == newY:
			return True
		return False

	# Check for any pieces intersecting lines x = a or y = a
	def collision_check(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		if xCoordinate == newX:
			left = min(yCoordinate, newY) + 1
			right = max(yCoordinate, newY)
			for i in range(left, right):
				if not board[xCoordinate][i] is None:
					return True
			return False

		if yCoordinate == newY:
			left = min(xCoordinate, newX) + 1
			right = max(xCoordinate, newX)
			for i in range(left, right):
				if not board[i][yCoordinate] is None:
					return True
			return False
		return True


	def print(self) -> str:
		return " ♜ "