from ChessPiece import ChessPiece

class Knight(ChessPiece):
	# The Knight moves in an L shape. 2 squares on an axis and 1 square on the other.
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		if (abs(xCoordinate - newX) == 2 and abs(yCoordinate - newY) == 1 ) or\
		   (abs(xCoordinate - newX) == 1 and abs(yCoordinate - newY) == 2):
			return True
		return False

	# The knight (who says NI!) can jump over obstacles.
	def collision_check(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		return False

	def print(self) -> str:
		return " ♞ "