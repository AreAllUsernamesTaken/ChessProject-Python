from ChessPiece import ChessPiece

class King(ChessPiece):
	# The King can move 1 square in any direction 
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		if (abs(xCoordinate - newX) <= 1 and abs(yCoordinate - newY) <= 1 ):
			return True
		return False

	# Pieces that move exactly one square dont have collisions
	def collisionCheck(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		return False

	def print(self) -> str:
		return " ♚ "