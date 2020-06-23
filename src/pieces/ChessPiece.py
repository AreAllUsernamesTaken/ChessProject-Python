from PieceColor import PieceColor

class ChessPiece:
	# Each piece only knows its own color (coordinates are the board's job).
	def __init__(self, pieceColor: PieceColor) -> None:
		self.pieceColor = pieceColor

	# Each piece must validate that, given a start point and an end point the move is legal.
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		pass

	# Furthermore each piece must validate there are no collisions along the way.
	def collision_check(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		pass

	# All pieces return their own ASCII representation (for drawing the board in terminal)
	def print(self) -> str:
		pass
