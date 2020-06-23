from ChessPiece import ChessPiece, PieceColor

class Pawn(ChessPiece):
	# The Pawn can move 2 tiles if in starting position (depends on color) 
	def __init__(self, pieceColor: PieceColor)-> None:
		if pieceColor not in PieceColor:
			raise TypeError("Invalid color.")

		self.PAWN_START = -1
		if pieceColor is PieceColor.WHITE:
			self.PAWN_START = 6
		if pieceColor is PieceColor.BLACK:
			self.PAWN_START = 1
		ChessPiece.__init__(self, pieceColor)
		
	# The pawn can only move forward, 1 square per turn (or 2 from starting position).
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		# Check for left/right movements
		if yCoordinate != newY:
			return False

		# White pawns can only go UP (decreasing on OX)
		if self.pieceColor == PieceColor.WHITE:
			if xCoordinate < newX or xCoordinate - newX > 2\
				or (xCoordinate - newX == 2 and xCoordinate != self.PAWN_START):
				return False
			return True

		# Black pawns can only go Down (increasing on OX)
		if self.pieceColor == PieceColor.BLACK:
			if xCoordinate > newX or newX - xCoordinate > 2\
				or (newX - xCoordinate == 2 and xCoordinate != self.PAWN_START):
				return False
			return True
		
		return False

	# The pawn is the only piece that has a special attack move, 1 square diagonaly.
	def attack(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		# Attack must be inflicted on an adjacent square
		if abs(yCoordinate - newY) != 1:
			return False

		# The attack may not go "behind"; pawns must advance towards the opponent.
		if self.pieceColor == PieceColor.WHITE:
			if xCoordinate - newX != 1:
				return False
			return True

		# The attack may not go "behind"; pawns must advance towards the opponent.
		if self.pieceColor == PieceColor.BLACK:
			if newx - xCoordinate != 1:
				return False
			return True

		return False

	# The pawn can move only 1 square. It never colides (either attacks or free square).
	def collision_check(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int, board: list) -> bool:
		return False

	def print(self) -> str:
		return " ♟︎ "