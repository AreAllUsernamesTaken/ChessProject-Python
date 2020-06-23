from PieceColor import PieceColor
class ChessPiece:
	def __init__(self, pieceColor: PieceColor) -> None:
		self.pieceColor = pieceColor

	def move(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		pass

	def attack(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		pass