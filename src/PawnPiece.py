from ChessPiece import ChessPiece, PieceColor

class Pawn(ChessPiece):
	def __init__(self, pieceColor: PieceColor)-> None:
		if pieceColor not in PieceColor:
			raise TypeError("Invalid color.")

		if pieceColor is PieceColor.WHITE:
			self.PAWN_START = 5
		if pieceColor is PieceColor.BLACK:
			self.PAWN_START = 1
		ChessPiece.__init__(self, pieceColor)
		
	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		if yCoordinate != newY:
			return False

		if self.pieceColor == PieceColor.WHITE:
			if xCoordinate < newX or xCoordinate - newX > 2\
				or (xCoordinate - newX == 2 and xCoordinate != self.PAWN_START):
				return False
			return True

		if self.pieceColor == PieceColor.BLACK:
			if xCoordinate > newX or newX - xCoordinate > 2\
				or (newX - xCoordinate == 2 and xCoordinate != self.PAWN_START):
				return False
			return True
		
		return False

	def attack(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		if abs(yCoordinate - newY) != 1:
			return False

		if self.pieceColor == PieceColor.WHITE:
			if xCoordinate - newX != 1:
				return False
			return True

		if self.pieceColor == PieceColor.BLACK:
			if newx - xCoordinate != 1:
				return False
			return True

		return False