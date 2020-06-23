from ChessPiece import ChessPiece
from BishopPiece import Bishop
from RookPiece import Rook
class Queen(Rook, Bishop):
	# The Queen can move perpendicularly (like a Rook) or diagonally(like a Bishop)
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		return Bishop.move(self, xCoordinate, yCoordinate, newX, newY) or\
			   Rook.move(self, xCoordinate, yCoordinate, newX, newY)

	# Depending on the movement type, the queen inherits the collision logic from Bishop or Rook
	def collision_check(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		if xCoordinate == newX or yCoordinate == newY:
			return Rook.collision_check(self, xCoordinate, yCoordinate, newX, newY, board)
		return Bishop.collision_check(self, xCoordinate, yCoordinate, newX, newY, board) 

	def print(self) -> str:
		return " ♛ "